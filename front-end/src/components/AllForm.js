import { MatchForm } from "./MatchForm.js";
import { NowLater } from "./NowLater.js";
import { Address } from "./Address.js";
import React from "react";
export function AllForm({
  setSubmit,
  startDate,
  setStartDate,
  address,
setFormData}) {
  const [isPage, setPage] = React.useState("Timing");
  const [backFunc, setBackFunc] = React.useState(false);
  const [forFunc, setForFunc] = React.useState(true);
  const [afSubmit, afSetSubmit] = React.useState(false);

  React.useEffect(() => {
    setSubmit(afSubmit);
  }, [setSubmit, afSubmit]);

  function submitHandler() {
    setFormData({
      "timing": startDate.toLocaleString(),
      "address": address.current.value
    })
    afSetSubmit(true);
  }

  function toggleForward() {
    if (isPage === "Timing") {
      setPage("Date");
      setBackFunc(true);
    } else if (isPage === "Date") {
      setPage("Destination");
      setForFunc(false);
    }
  }

  function toggleBackward() {
    if (isPage === "Destination") {
      setPage("Date");
      setForFunc(true);
    } else if (isPage === "Date") {
      setPage("Timing");
      setBackFunc(false);
    }
  }

  function correctPage(currentPage) {
    switch (currentPage) {
      case "Timing":
        return <NowLater></NowLater>;
      case "Date":
        return (
          <MatchForm
            startDate={startDate}
            setStartDate={setStartDate}
          ></MatchForm>
        );
      case "Destination":
        return <Address address={address}></Address>;
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
