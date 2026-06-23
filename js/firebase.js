// Firebase configuration and shared utilities
const firebaseConfig = {
  apiKey: "AIzaSyAH3xQ74P7tGMNueJmOw1ty_ucufffa7VU",
  authDomain: "pyspark-sql-courses.firebaseapp.com",
  projectId: "pyspark-sql-courses",
  storageBucket: "pyspark-sql-courses.firebasestorage.app",
  messagingSenderId: "253980650849",
  appId: "1:253980650849:web:8c60f55f59122de49d6920",
  measurementId: "G-MRXMR7NTLN"
};

if (!firebase.apps.length) firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();

let currentUser = null;

auth.onAuthStateChanged(user => {
  currentUser = user;
  document.querySelectorAll('[data-auth-show]').forEach(el => el.style.display = user ? '' : 'none');
  document.querySelectorAll('[data-auth-hide]').forEach(el => el.style.display = user ? 'none' : '');
  const pill = document.getElementById('user-pill');
  const signinBtn = document.getElementById('signin-btn');
  if (pill && signinBtn) {
    if (user) {
      pill.classList.add('visible');
      signinBtn.style.display = 'none';
      const av = pill.querySelector('.user-avatar');
      if (av) av.textContent = (user.displayName || user.email || 'U').charAt(0).toUpperCase();
      const name = pill.querySelector('.user-name');
      if (name) name.textContent = user.displayName || user.email.split('@')[0];
    } else {
      pill.classList.remove('visible');
      signinBtn.style.display = '';
    }
  }
  if (user && typeof onUserReady === 'function') onUserReady(user);
  loadStreakBadge();
});

function getDoc() {
  if (!currentUser) return null;
  return db.collection('users').doc(currentUser.uid);
}

async function loadUserData() {
  if (!currentUser) {
    try { return JSON.parse(localStorage.getItem('lwm_data') || '{}'); } catch { return {}; }
  }
  try {
    const snap = await getDoc().get();
    return snap.exists ? snap.data() : {};
  } catch { return {}; }
}

async function saveUserData(data) {
  if (!currentUser) {
    try {
      const existing = JSON.parse(localStorage.getItem('lwm_data') || '{}');
      localStorage.setItem('lwm_data', JSON.stringify({ ...existing, ...data }));
    } catch {}
    return;
  }
  try { await getDoc().set(data, { merge: true }); } catch (e) { console.warn(e); }
}

async function markTopicComplete(topicId) {
  const data = await loadUserData();
  const completed = data.completed || [];
  if (!completed.includes(topicId)) {
    completed.push(topicId);
    await saveUserData({ completed, lastActivity: Date.now() });
    updateSidebarProgress(completed);
    showToast('Topic completed! +1 XP', 'success');
  }
}

async function saveQuizScore(topicId, score, total) {
  const data = await loadUserData();
  const quizzes = data.quizzes || {};
  quizzes[topicId] = { score, total, ts: Date.now() };
  let streak = data.streak || 0;
  const last = data.lastQuizDate || 0;
  const today = new Date().toDateString();
  const lastDay = new Date(last).toDateString();
  if (lastDay !== today) streak++;
  await saveUserData({ quizzes, streak, lastQuizDate: Date.now() });
  loadStreakBadge();
}

async function loadStreakBadge() {
  const badge = document.getElementById('streak-badge');
  if (!badge) return;
  const data = await loadUserData();
  const streak = data.streak || 0;
  badge.textContent = streak + ' day streak';
  badge.style.display = streak > 0 ? '' : 'none';
}

function updateSidebarProgress(completed) {
  document.querySelectorAll('[data-topic]').forEach(el => {
    const tid = el.dataset.topic;
    const check = el.querySelector('.sidebar-check');
    if (completed.includes(tid)) {
      el.classList.add('completed');
      if (check) check.textContent = '✓';
    }
  });
}

// Copy button
document.addEventListener('click', e => {
  const btn = e.target.closest('.copy-btn');
  if (!btn) return;
  const block = btn.closest('.code-block');
  if (!block) return;
  const pre = block.querySelector('pre');
  const text = pre ? pre.innerText : '';
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
  });
});

// Accordion / Interview card
document.addEventListener('click', e => {
  const iq = e.target.closest('.interview-q');
  if (iq) iq.closest('.interview-card').classList.toggle('open');
});

// Auth modal
function openAuth() { document.getElementById('auth-modal')?.classList.add('open'); }
function closeAuth() { document.getElementById('auth-modal')?.classList.remove('open'); }

async function signInGoogle() {
  const p = new firebase.auth.GoogleAuthProvider();
  try {
    await auth.signInWithPopup(p);
    closeAuth();
    showToast('Signed in!', 'success');
  } catch(e) { showToast(e.message, 'error'); }
}

async function signInEmail() {
  const email = document.getElementById('auth-email')?.value;
  const pass = document.getElementById('auth-pass')?.value;
  if (!email || !pass) { showToast('Enter email and password', 'error'); return; }
  try {
    await auth.signInWithEmailAndPassword(email, pass);
    closeAuth(); showToast('Signed in!', 'success');
  } catch {
    try {
      await auth.createUserWithEmailAndPassword(email, pass);
      closeAuth(); showToast('Account created!', 'success');
    } catch(e) { showToast(e.message, 'error'); }
  }
}

async function signOut() {
  await auth.signOut();
  showToast('Signed out');
  setTimeout(() => location.reload(), 500);
}

// Toast
function showToast(msg, type = '') {
  let t = document.getElementById('global-toast');
  if (!t) {
    t = document.createElement('div');
    t.id = 'global-toast';
    t.className = 'toast';
    document.body.appendChild(t);
  }
  t.textContent = msg;
  t.className = 'toast' + (type ? ' ' + type : '');
  requestAnimationFrame(() => t.classList.add('show'));
  clearTimeout(t._timer);
  t._timer = setTimeout(() => t.classList.remove('show'), 2800);
}

// Quiz engine
function initQuiz(containerId, questions, topicId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  let score = 0;
  let answered = 0;
  container.innerHTML = '';

  questions.forEach((q, qi) => {
    const qEl = document.createElement('div');
    qEl.className = 'quiz-question fade-in';
    qEl.style.animationDelay = (qi * 0.08) + 's';

    const opts = q.options.map((o, oi) => {
      const letters = ['A','B','C','D'];
      return `<div class="quiz-option" data-qi="${qi}" data-oi="${oi}">
        <span class="opt-letter">${letters[oi]}</span>
        <span>${o}</span>
      </div>`;
    }).join('');

    qEl.innerHTML = `
      <div class="quiz-question-text">${qi+1}. ${q.question}</div>
      <div class="quiz-options">${opts}</div>
      <div class="quiz-explanation" id="qe-${containerId}-${qi}">${q.explanation || ''}</div>
    `;
    container.appendChild(qEl);
  });

  const resultEl = document.createElement('div');
  resultEl.className = 'quiz-result';
  resultEl.id = 'qr-' + containerId;
  container.appendChild(resultEl);

  container.addEventListener('click', async e => {
    const opt = e.target.closest('.quiz-option');
    if (!opt) return;
    const qi = parseInt(opt.dataset.qi);
    const oi = parseInt(opt.dataset.oi);
    const qBlock = opt.closest('.quiz-question');
    if (qBlock.classList.contains('answered')) return;
    qBlock.classList.add('answered');
    answered++;

    const allOpts = qBlock.querySelectorAll('.quiz-option');
    allOpts.forEach(o => o.classList.add('disabled'));

    const correct = questions[qi].correct;
    if (oi === correct) {
      opt.classList.add('correct');
      score++;
    } else {
      opt.classList.add('wrong');
      allOpts[correct].classList.add('correct');
    }

    const expEl = document.getElementById('qe-' + containerId + '-' + qi);
    if (expEl) expEl.classList.add('show');

    if (answered === questions.length) {
      const pct = Math.round((score / questions.length) * 100);
      const pass = pct >= 70;
      resultEl.className = 'quiz-result show ' + (pass ? 'pass' : 'fail');
      resultEl.innerHTML = pass
        ? `<span>🎉</span> <span>You scored ${score}/${questions.length} (${pct}%) - Passed!</span>`
        : `<span>💡</span> <span>You scored ${score}/${questions.length} (${pct}%) - Review and retry</span>`;
      if (topicId) await saveQuizScore(topicId, score, questions.length);
    }
  });
}

// Sidebar active state on scroll
function initScrollSpy() {
  const sections = document.querySelectorAll('[data-section]');
  if (!sections.length) return;
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.dataset.section;
        document.querySelectorAll('.sidebar-item, .sidebar-sub-item').forEach(el => {
          el.classList.toggle('active', el.dataset.target === id);
        });
      }
    });
  }, { threshold: 0.3 });
  sections.forEach(s => observer.observe(s));
}

function scrollToSection(id) {
  const el = document.getElementById(id) || document.querySelector('[data-section="' + id + '"]');
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

document.addEventListener('DOMContentLoaded', async () => {
  initScrollSpy();
  const data = await loadUserData();
  if (data.completed) updateSidebarProgress(data.completed);
  const badge = document.getElementById('streak-badge');
  if (badge) {
    const streak = data.streak || 0;
    badge.textContent = '🔥 ' + streak + ' day streak';
    badge.style.display = streak > 0 ? '' : 'none';
  }
});
