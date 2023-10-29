export function Passengers({pax, setPax, paxFill}) {
    return (
      <div class="col-auto">
        <div class="prompt">How many people are traveling <br></br>(including you)?</div>
        <div class="addressholder">
          <input
            type="text"
            value={pax}
            pattern="[0-9]*"
            onChange={(e) => paxFill(e)}
          ></input>
        </div>
      </div>
    );
  }
  