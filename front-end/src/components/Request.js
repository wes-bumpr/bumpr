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
            <div class="card-header">Anna Z.</div>
            <ul class="list-group list-group-flush">
              <div class="list-group-item">
                <small>Departure Time</small>
                <div class="mb-1">{formData["timing"]}</div>
              </div>
              <div class="list-group-item">
                <small>Destination Address</small>
                <div class="mb-1">{formData["address"]}</div>
              </div>
              <div class="list-group-item">
                <small>Number of Passengers</small>
                <div class="mb-1">1</div>
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
