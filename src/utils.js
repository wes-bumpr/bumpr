import { useState } from 'react'
import axios from "axios";
// const SERVER_ORIGIN = '';
 
// const rrUrl = `${SERVER_ORIGIN}/ride-request`;
 
// export function rideRequest(data) {
//   // param data: a list of dictionary ride requests
//   // example: ride_requests = [{"depart_time": 1000, "user_ID": "C1024851", "destination_address": {"city": "Needham", "state": "MA"}},
//   //                          {"depart_time": 1050, "user_ID": "C1000001", "destination_address": {"city": "Wellesley", "state": "MA"}}]
//   return fetch(rrUrl, {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify(data)
//   }).then((response) => {
//     if (response.status !== 200) {
//       throw Error('Fail to make request');
//     }
 
//     return response.json();
//   })
// }


const SERVER_ORIGIN = '';
const rrUrl = "/ride-request";
export function rideRequest(data) {
  // param data: a list of dictionary ride requests
  // example: ride_requests = [{"depart_time": 1000, "user_ID": "C1024851", "destination_address": {"city": "Needham", "state": "MA"}},
  //                          {"depart_time": 1050, "user_ID": "C1000001", "destination_address": {"city": "Wellesley", "state": "MA"}}]
  // return fetch(rrUrl, {
  //   method: 'POST',
  //   headers: {
  //     'Content-Type': 'application/json',
  //   },
  //   body: JSON.stringify(data)
  // }).then((response) => {
  //   if (response.status !== 200) {
  //     throw Error('Fail to make request');
  //   }
  //   return response.json();
  // })
//   $.post( rrUrl, { toSubmit })
//     .fail(function() {
//       alert( "$.post failed!" );
//     });
// }
// toSubmit = JSON.stringify(data); //could alternatively use .serialize()
console.log(data)
axios({
  method: "POST",
  url: "/ride-request",
  data:
    data,
})
  .then((response) => {
    const res = response.data;
    console.log('Request successful:', res);
  })
  .catch((error) => {
    if (error.response) {
      console.log('Request failed:', error.response.status);
      console.log('Response data:', error.response.data);
      console.log('Response headers:', error.response.headers);
    }
  });
}

// export function MatchRequest(userID) {
// //   const [matches, setMatches] = useState(null);
// //   const [loading, setLoading] = useState(true);
// //   const [error, setError] = useState(null);
// //   const [card, setCard] = useState(null)
// //  const userID = 'C10000342' //this is temporary
// //   //this is request for the matches -- maybe need to provide data so that backend knows which matches we want, or I need to know the matchID so I can filter data
// //   useEffect(() => {
// //     fetch(`https://bumpr/matches/${userID}`, {'methods':'GET'}) //this will need to be changed also need to figure out matchID, like how to request the one that i want, or will they know
// //       .then(response => response.json()) //what is this doing?
// //       .then((data) => {
// //         console.log(data);
// //         setLoading(false);
// //         data.ride_request_ID.forEach((rideID) => {
// //             fetch(`https://bumpr/ride-requests/${userID}`, {'methods':'GET'}) //this will need to be changed
// //                 .then(response => response.json())
// //                 .then((match) => {
// //                     console.log(match);
// //                     setLoading(false);
// //                     const info = {name:{rideID}, destination:match.destination_address, arrivalTime:match.destination_time}
// //                     setCard({info})
// //       })
// //       .catch((e) => {
// //         console.error(`An error occurred: ${e}`)
// //       });
// //             setMatches((arr) => [...arr, matchID])
// //         })
// //       })
// //       .catch((e) => {
// //         console.error(`An error occurred: ${e}`)
// //       });
// //   }, []);
// //   function Success(){
// //     if (card){
// //         return(
// //             <div>
// //                 <div class="prompt">You have matched with...</div>
// //                 <div class="body">{info}</div>
// //                 <div className="card text-center m-3">
// //                     <h5 className="card-header">Name: {card.name}</h5>
// //                                 <div className="card-body">
// //                                     Destination: {card.destination}
// //                                 </div>
// //                         {loading && <p>Loading...</p>}
// //                         {!loading && <p>Fetched data</p>}
// //                 </div>
// //             </div>
// //     )}
// //     else{
// //         return(
// //             <div>
// //                 <div class="prompt">You did not match with anyone.</div>
// //                 <div class="prompt">We will notify you if you recieve a new match before your date.</div>
// //             </div>
// //     )}
// // }
// //   return (<Success/>)
//   $.get( rrUrl, userID, function (data) {
//     const date = data.date;
//     const depart_time = data.departure_time;
//   })
//     .done(function(card) {
//         return(
//            <div>
//              <div class="prompt">You have matched with...</div>
//                 <div class="body">{info}</div>
//                   <div className="card text-center m-3">
//                     <h5 className="card-header">Name: {card.name}</h5>
//                       <div className="card-body">
//                           Destination: {card.destination}
//                       </div>
//                       <p>Loading...</p>
//                       <p>Fetched data</p>
//                   </div>
//             </div>
//             )}
//             )
//     .fail(function() {
//       return(
//         <div>
//             <div class="prompt">You did not match with anyone.</div>
//             <div class="prompt">We will notify you if you recieve a new match before your date.</div>
//         </div>
//     )});
// }