// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getFirestore} from "firebase/firestore"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDfBxy0PQ12cxYG-5H1cQ9_420Jw23nfX4",
  authDomain: "carpishop-8f2cc.firebaseapp.com",
  projectId: "carpishop-8f2cc",
  storageBucket: "carpishop-8f2cc.appspot.com",
  messagingSenderId: "691418411492",
  appId: "1:691418411492:web:8ae091ea7f15ed1c56d7f1",
  measurementId: "G-P5XGGJFDWR"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
const analytics = getAnalytics(app);