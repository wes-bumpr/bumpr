// import '/Users/ellaboodell/bumpr/src/static/style.css';
import React from 'react';

export function MatchResults({formdata}) {
    return (
        <center>
            <div class="prompt">You matched with...</div>
            {/* w-50 bg-primary mb-3 */}
            {/* style={width= '50rem', color='#46C9DA'} */}
            <div class="card w-50 bg-primary mb-3">  
                <div class="card-header">
                    email
                    {/* Contact Information: {formdata.riders[1]} */}
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Departure Location: </li>
                    {/* <li class="list-group-item">Departure Location: {formdata.from}</li>
                    <li class="list-group-item">Departure Time: {formdata.depart_time}</li>
                    <li class="list-group-item">Destination: {formdata.to}</li> */}
                </ul>
            </div>

            {/* <div class="prompt w-75">You are going to {formdata.to} at {formdata.depart_time}</div> */}
    </center>
    )
}
