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
  document.querySelectorAll('.auth-show').forEach(el => el.classList.toggle('hidden', !user));
  document.querySelectorAll('.auth-hide').forEach(el => el.classList.toggle('hidden', !!user));
  if (user && typeof onUserReady === 'function') onUserReady(user);
});

function getDoc() {
  if (!currentUser) return null;
  return db.collection('users').doc(currentUser.uid);
}

async function loadUserData() {
  if (!currentUser) return null;
  try {
    const snap = await getDoc().get();
    return snap.exists ? snap.data() : {};
  } catch { return {}; }
}

async function setField(key, val) {
  if (!currentUser) { localStorage.setItem(key, JSON.stringify(val)); return; }
  try { await getDoc().set({ [key]: val }, { merge: true }); } catch (e) { console.warn(e); }
}

async function addToArray(key, val) {
  if (!currentUser) {
    const arr = JSON.parse(localStorage.getItem(key) || '[]');
    if (!arr.includes(val)) arr.push(val);
    localStorage.setItem(key, JSON.stringify(arr));
    return;
  }
  try {
    await getDoc().set({ [key]: firebase.firestore.FieldValue.arrayUnion(val) }, { merge: true });
  } catch (e) { console.warn(e); }
}

async function removeFromArray(key, val) {
  if (!currentUser) {
    const arr = JSON.parse(localStorage.getItem(key) || '[]').filter(v => v !== val);
    localStorage.setItem(key, JSON.stringify(arr));
    return;
  }
  try {
    await getDoc().set({ [key]: firebase.firestore.FieldValue.arrayRemove(val) }, { merge: true });
  } catch (e) { console.warn(e); }
}

// Toast
function showToast(msg, type = '') {
  let t = document.querySelector('.toast');
  if (!t) { t = document.createElement('div'); t.className = 'toast'; document.body.appendChild(t); }
  t.textContent = msg;
  t.className = 'toast' + (type ? ' ' + type : '');
  requestAnimationFrame(() => { t.classList.add('show'); });
  setTimeout(() => t.classList.remove('show'), 2600);
}

// Copy button handler
document.addEventListener('click', e => {
  const btn = e.target.closest('.copy-btn');
  if (!btn) return;
  const pre = btn.closest('.code-block').querySelector('pre');
  navigator.clipboard.writeText(pre.innerText).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1800);
  });
});

// Accordion handler
document.addEventListener('click', e => {
  const h = e.target.closest('.accord-head');
  if (h) h.closest('.accord').classList.toggle('open');
  const iq = e.target.closest('.iq-q');
  if (iq) iq.closest('.iq-item').classList.toggle('open');
});

// Auth modal
function openAuth() { document.getElementById('auth-modal')?.classList.add('open'); }
function closeAuth() { document.getElementById('auth-modal')?.classList.remove('open'); }

async function signInGoogle() {
  const p = new firebase.auth.GoogleAuthProvider();
  try { await auth.signInWithPopup(p); closeAuth(); showToast('Signed in!', 'success'); }
  catch(e) { showToast(e.message, 'error'); }
}

async function signInEmail(email, pass) {
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

async function signOut() { await auth.signOut(); showToast('Signed out'); location.reload(); }
