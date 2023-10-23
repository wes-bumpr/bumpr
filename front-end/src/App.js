import "./static/style.css";
import { Navbar } from "./components/Navbar.js";
import { AllForm } from "./components/AllForm.js";
import { RideRequest } from "./components/Request.js";
import { OpenStreetMapProvider } from "leaflet-geosearch";
import React from "react";
import {rideRequest} from "utils.js";


export default function App() {

  const provider = new OpenStreetMapProvider({
    params: {
      "accept-language": "en",
      countrycodes: "us",
    },
  });
  const [coords, setCoords] = React.useState()
  const [text, setText] = React.useState([]);
  const [searchResults, setSearchResults] = React.useState([]);
  const [isSubmit, setSubmit] = React.useState(false);
  const [startDate, setStartDate] = React.useState(new Date());
  const address = React.useRef(null);
  const [formData, setFormData] = React.useState({
    timing: "",
    address: "",
    coords: {'x':0, 'y':0},
  });

  async function autocomplete(address) {
    setText(address);
    const results = await provider.search({ query: text });
    setSearchResults(results);
  }

  function addressSelect(label, x, y) {
    setText(label)
    setCoords({'x':x,'y':y})
  }

  function submitHandler() {
    setFormData({
      timing: startDate.toLocaleString(),
      address: text,
      coords: coords,
    });
    setSubmit(true);
    rideRequest(formData);
  }

  return (
    <>
      <Navbar />
      {isSubmit ? (
        <RideRequest formData={formData} />
      ) : (
        <AllForm
          startDate={startDate}
          setStartDate={setStartDate}
          address={address}
          text={text}
          setText={setText}
          searchResults={searchResults}
          setSearchResults={setSearchResults}
          autocomplete={autocomplete}
          submitHandler={submitHandler}
          setCoords={setCoords}
          addressSelect={addressSelect}
        />
      )}

    </>
  );
}
