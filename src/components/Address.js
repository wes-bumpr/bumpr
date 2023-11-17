export function Address({
  text,
  searchResults,
  autocomplete,
  addressSelect,
  sAddress
}) {

  return (
    <div class="col-auto">
      <div class="prompt">Where are you coming from?</div>
      <div class="selected_address">{sAddress}</div>
      <div class="addressholder">
        <input
          type="text"
          value={text}
          onChange={(e) => autocomplete(e.target.value)}
        ></input>
        <div class="list-group addressresults">
          {searchResults.map((item) => (
            <button
              href=""
              class="list-group-item list-group-item-action"
              aria-current="true"
              onClick={(e)=>addressSelect(e.target.innerText, item.x, item.y)}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
