import { useState, useRef, props } from "react";
import Autocomplete, { usePlacesWidget } from "react-google-autocomplete";

const API_KEY = "AIzaSyDPEM_aToQcxAGHlz-MYGhuvaE4wkziONA";

export function Address({ address }) {
  const country = "us";
  return (
    <div class="col-auto">
      <div class="prompt">Where would you like to go?</div>
      <div class="addressholder">
        <Autocomplete
          style={{ width: "100%" }}
          ref={address}
          apiKey={API_KEY}
          onPlaceSelected={(selected, a, c) => {
            console.log(selected);
          }}
          options={{
            types: ["geocode", "establishment"],
            componentRestrictions: { country },
          }}
          className="form-control"
        />
      </div>
    </div>
  );
}
