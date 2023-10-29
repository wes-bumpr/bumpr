import { Timing } from "./Timing.js";
import { Address } from "./Address.js";
import { AddressTo } from "./AddressTo.js";
import { Passengers } from "./Passengers.js";
import React from "react";
export function AllForm({
  startDate,
  setStartDate,
  text,
  setText,
  searchResults,
  searchResultsTo,
  autocomplete,
  autocompleteTo,
  submitHandler,
  setCoords,
  addressSelect,
  sAddress,
  toText,
  setToText,
  setToCoords,
  addressSelectTo,
  sToAddress,
  pax,
  setPax
}) {
  const [isPage, setPage] = React.useState("Date");
  const [backFunc, setBackFunc] = React.useState(false);
  const [forFunc, setForFunc] = React.useState(true);

  function toggleForward() {
    if (isPage === "Date") {
      setPage("Start");
      setBackFunc(true);
    } else if (isPage === "Start") {
      setPage("Destination");
    } else if (isPage === "Destination") {
      setPage("Passengers")
      setForFunc(false);
    }
  }

  function toggleBackward() {
    if (isPage === "Start") {
      setPage("Date");
      setBackFunc(false);
  } else if (isPage === "Destination") {
      setPage("Start");
  } else if (isPage === "Passengers") {
      setPage("Destination");
      setForFunc(true);
  }
}

  function correctPage(currentPage) {
    switch (currentPage) {
      case "Date":
        return (
          <Timing startDate={startDate} setStartDate={setStartDate}></Timing>
        );
      case "Start":
        return (
          <Address
            text={text}
            setText={setText}
            searchResults={searchResults}
            autocomplete={autocomplete}
            setCoords={setCoords}
            addressSelect={addressSelect}
            sAddress={sAddress}
          ></Address>
        );
      case "Destination":
        return (
          <AddressTo
            searchResultsTo={searchResultsTo}
            autocompleteTo={autocompleteTo}
            toText={toText}
            setToText={setToText}
            setToCoords={setToCoords}
            addressSelectTo={addressSelectTo}
            sToAddress={sToAddress}></AddressTo>
        )
      case "Passengers":
        return (
          <Passengers pax={pax} setPax={setPax}></Passengers>
        )
      default:
        return (
          <Timing startDate={startDate} setStartDate={setStartDate}></Timing>
        );
    }
  }

  return (
    <div class="container">
      <div class="row promptholder align-items-center justify-content-center">
        <div class="col-auto">
          {backFunc ? (
            <button class="caret-circle backbutton" onClick={toggleBackward}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-caret-left-fill"
                viewBox="0 0 16 16"
              >
                <path d="m3.86 8.753 5.482 4.796c.646.566 1.658.106 1.658-.753V3.204a1 1 0 0 0-1.659-.753l-5.48 4.796a1 1 0 0 0 0 1.506z" />
              </svg>
            </button>
          ) : null}
        </div>
        {correctPage(isPage)}
        <div class="col-auto">
          {forFunc ? (
            <button class="caret-circle" onClick={toggleForward}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-caret-right-fill"
                viewBox="0 0 16 16"
              >
                <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
              </svg>
            </button>
          ) : (
            <button class="caret-circle" onClick={submitHandler}>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                fill="currentColor"
                class="bi bi-caret-right-fill"
                viewBox="0 0 16 16"
              >
                <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
              </svg>
            </button>
          )}
        </div>
      </div>
    </div>
  );
}