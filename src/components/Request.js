import React from "react";
export function RideRequest({ formData }) {
  return (
    <div class="container">
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
        <button type="button" class="btn btn-info mt-5 contbutton">Continue</button>

        </div>
        </div>
        
      </div>
    </div>
  );
}
