//TODO: make sure we are getting the match data from the backend to display
import React from "react";
export function RideResult({ formData, profileData }) {
  const [isContinue, setContinue] = React.useState(false);
  console.log("in request.js" + profileData)
  function showResult(isContinue) {
    if (isContinue) {
      if (profileData){
        return (
      <div class="row promptholder align-items-center justify-content-center">
        <div class="row align-items-center justify-content-center">
          <div class="prompt mb-5">
          You matched with...
          </div>
          <div class="card px-0 ridereq">
            <div class="card-header">Your match: {profileData["users"][0]} and profileData["users"][1]</div>
            <ul class="list-group list-group-flush">
              <div class="list-group-item">
                <small>Departure Time</small>
                <div class="mb-1">{profileData["depart_time"]}</div>
              </div>
              <div class="list-group-item">
                <small>Your Departure Addresses</small>
                <div class="mb-1">{profileData["origin"][0]} and profileData["origin"][1]</div>
              </div>
              <div class="list-group-item">
                <small>Your Destination Addresses</small>
                <div class="mb-1">{formData["to"][0]} and {formData["to"][0]}</div>
              </div>
            </ul>
          </div>
          <div class="row justify-content-center">
          <div class="prompt mb-5">You are leaving at {profileData.depart_time}</div>
        </div>
        </div>
      </div>
     ) } else if (profileData == "No Match") {
      return (
          <div class="prompt mb-5">
            You did not match with anyone.
            We will notify you if you receive a new match before your date.
            </div>
      )} else {
        return (
          <div class="prompt mb-5">error retrieving match data: {profileData}</div>
        )
      }

    }
    else {
      return (
      <div class="row promptholder align-items-center justify-content-center">
        <div class="row align-items-center justify-content-center">
          <div class="prompt mb-5">
            You have created the following ride request:
          </div>
          <div class="card px-0 ridereq">
            <div class="card-header">{formData["user_ID"]}</div>
            <ul class="list-group list-group-flush">
              <div class="list-group-item">
                <small>Departure Time</small>
                <div class="mb-1">{formData["depart_time"]}</div>
              </div>
              <div class="list-group-item">
                <small>Departure Address</small>
                <div class="mb-1">{formData["origin_address"]}</div>
              </div>
              <div class="list-group-item">
                <small>Destination Address</small>
                <div class="mb-1">{formData["destination_address"]}</div>
              </div>
              <div class="list-group-item">
                <small>Number of Passengers</small>
                <div class="mb-1">{formData["total_num_people_traveling"]}</div>
              </div>
            </ul>
          </div>
          <div class="row justify-content-center">
        <button type="button" class="btn btn-info mt-5 contbutton" onClick={setContinue}>Continue</button>
        </div>
        </div>
      </div>
    )}
  }
  return (
    <div class="container">
    {showResult(isContinue)}
    </div>
  );
}