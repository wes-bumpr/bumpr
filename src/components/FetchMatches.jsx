import { useState, useEffect } from "react";
 
export default function FetchMatches() {
 
  const [matches, setMatches] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [card, setCard] = useState(null)
 
  //this is request for the matches -- maybe need to provide data so that backend knows which matches we want, or I need to know the matchID so I can filter data
  useEffect(() => {
    fetch(`https://bumpr/matches`) //this will need to be changed
      .then(response => response.json())
      .then((data) => {
        console.log(data);
        setLoading(false);
        data.ride_request_ID.forEach((matchID) => {//rn i am accessing every matchID for every match
            fetch(`https://bumpr/ride-requests/${matchID}`) //this will need to be changed
                .then(response => response.json())
                .then((match) => {
                    console.log(match);
                    setLoading(false);
                    const info = {name:{matchID}, destination:match.destination_address, arrivalTime:match.destination_time}

                    setCard({info})
      })
      .catch((e) => {
        console.error(`An error occurred: ${e}`)
      });
            setMatches((arr) => [...arr, matchID])
        })
      })
      .catch((e) => {
        console.error(`An error occurred: ${e}`)
      });
  }, []);

  function Success(){
    if (card){
        return(
            <div>
                <div class="prompt">You have matched with...</div>
                <div class="body">{info}</div>
                <div className="card text-center m-3">
                    <h5 className="card-header">Name: {card.name}</h5>
                                <div className="card-body">
                                    Destination: {card.destination}
                                </div>
                        {loading && <p>Loading...</p>}
                        {!loading && <p>Fetched data</p>}
                </div>
            </div>
    )}
    else{
        return(
            <div>
                <div class="prompt">You did not match with anyone.</div>
                <div class="prompt">We will notify you if you recieve a new match before your date.</div>
            </div>
    )}
}
 
  return (<Success/>)
}
