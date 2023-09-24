// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
//import { getAnalytics } from "firebase/analytics";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAhw3p7cqnaQmczTxfUAts4lLfMLWJYG5Y",
  authDomain: "bumpr-db1f3.firebaseapp.com",
  databaseURL: "https://bumpr-db1f3-default-rtdb.firebaseio.com",
  projectId: "bumpr-db1f3",
  storageBucket: "bumpr-db1f3.appspot.com",
  messagingSenderId: "445089194671",
  appId: "1:445089194671:web:92a93daa9a04f9e3812a5a",
  measurementId: "G-004D5PV8F1"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);