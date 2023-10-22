import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useState } from "react";

export function MatchForm({startDate, setStartDate}) {
  return (
    <div class="col-auto">
      <div class="prompt">When do you need<br></br>this ride by?</div>
      <div class="dateholder">
        <DatePicker
          selected={startDate}
          onChange={(date) => setStartDate(date)}
          minDate={new Date()}
          timeInputLabel="Time:"
          dateFormat="MM/dd/yyyy h:mm aa"
          showTimeInput
          inline
        />
      </div>
    </div>
  );
}
