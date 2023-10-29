import "./static/style.css";
import { Navbar } from "./components/Navbar.js";
import { AllForm } from "./components/AllForm.js";
import { RideRequest } from "./components/Request.js";
import { OpenStreetMapProvider } from "leaflet-geosearch";
import React from "react";
// import {rideRequest} from "./utils.js";


export default function App() {

  const provider = new OpenStreetMapProvider({
    params: {
      "accept-language": "en",
      countrycodes: "us",
    },
  });
  const [disable, setDisable] = React.useState(false);
  const [pax, setPax] = React.useState('1');
  const [coords, setCoords] = React.useState();
  const [toCoords, setToCoords] = React.useState();
  const [text, setText] = React.useState([]);
  const [toText, setToText] = React.useState([]);
  const [searchResults, setSearchResults] = React.useState([]);
  const [searchResultsTo, setSearchResultsTo] = React.useState([]);
  const [isSubmit, setSubmit] = React.useState(false);
  const [startDate, setStartDate] = React.useState(new Date());
  const address = React.useRef(null);
  const toAddress = React.useRef(null);
  const [sAddress, setsAddress] = React.useState('No address selected');
  const [sToAddress, setsToAddress] = React.useState('No address selected');
  const [formData, setFormData] = React.useState({
    timing: "",
    from_address: "",
    to_address: "",
    num_passengers: 0,
    from_coords: {'x':0, 'y':0},
    to_coords: {'x':0, 'y':0}
  });

  async function autocomplete(a) {
    setText(a);
    const results = await provider.search({ query: text });
    setSearchResults(results);
  }

  async function autocompleteTo(a) {
    setToText(a);
    const results = await provider.search({ query: toText });
    setSearchResultsTo(results);
  }

  function addressSelect(label, x, y) {
    setText(label)
    setCoords({'x':x,'y':y})
    setsAddress(label)
    setDisable(false)
  }

  function paxFill(num) {
    setPax(num.target.value.replace(/\D/,''))
    if ((num.target.value.replace(/\D/,'')).length > 0) {
      setDisable(false);
    } else {
      setDisable(true)
    }
  }

  function addressSelectTo(label, x, y) {
    setToText(label)
    setToCoords({'x':x,'y':y})
    setsToAddress(label)
    setDisable(false)
  }

  function submitHandler() {
    setFormData({
      timing: startDate.toLocaleString(),
      from_address: sAddress,
      from_coords: coords,
      num_passengers: pax,
      to_address: sToAddress,
      to_coords: toCoords,
    });
    console.log(formData);
    setSubmit(true);
    // rideRequest(formData);
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
          toAddress={toAddress}
          toText={toText}
          setToText={setToText}
          searchResults={searchResults}
          setSearchResults={setSearchResults}
          searchResultsTo={searchResultsTo}
          setSearchResultsTo={setSearchResultsTo}
          autocomplete={autocomplete}
          autocompleteTo={autocompleteTo}
          submitHandler={submitHandler}
          setCoords={setCoords}
          addressSelect={addressSelect}
          sAddress={sAddress}
          setToCoords={setToCoords}
          addressSelectTo={addressSelectTo}
          sToAddress={sToAddress}
          pax = {pax}
          setPax={setPax}
          disable={disable}
          setDisable={setDisable}
          paxFill={paxFill}
        />
      )}

    </>
  );
}
