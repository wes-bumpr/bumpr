// Import Firestore database
import db from './firebase';
import { useState } from 'react';

export function MatchResults(request) {
    const [info, setInfo] = useState([]);
    const [names, setNames] = useState([])
    
    const Read = () => {
    
        // Start the fetch operation as soon as
        // the page loads
        window.addEventListener('load', () => {
            Fetchdata();
        });
    
        // Fetch the required data using the get() method
        const Fetchdata = () => {
            db.collection("matches").get().then((querySnapshot) => {
     
                // Loop through the data and store
                // it in array to display
                querySnapshot.forEach(element => {
                    var matches = element.matches();
                    setInfo(arr => [...arr, matches]);
                });
            })
        }
    }

    function getNames(){
        info.forEach(match => {
            if (match == request){
                match.matched_people.forEach(personID => {
                    setNames(arr => [...arr, personID]) //todo austen would it be possible to store peoples names rather than ID nums here
                })
            }
        })
    }

    function success(){
        if (names.length <= 1){
            return(
            <div>
                <div class="prompt">You did not match with anyone.</div>
                <div class="prompt">We will notify you if you recieve a new match before your date.</div>
            </div>)
        }
        else{
            return(
                <div>
                    <div class="prompt">You have matched with...</div>
                    <div class="body">{info}</div>
                    <center>
                        names.map((label) => (
                            <button class='button-style' name={label}/>
                        ))
                    </center>
                </div>
        )}
    }

        // Display the result on the page
        return (
            <success></success>
        );
    }