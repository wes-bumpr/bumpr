export function Passengers({pax, setPax}) {
    return (
      <div class="col-auto">
        <div class="prompt">How many people are traveling <br></br>(including you)?</div>
        <div class="addressholder">
          <input
            type="text"
            value={pax}
            onChange={(e) => setPax(e)}
          ></input>
        </div>
      </div>
    );
  }
  