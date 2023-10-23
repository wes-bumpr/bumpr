export function Address({
  text,
  setText,
  searchResults,
  autocomplete,
  addressSelect,
}) {
  return (
    <div class="col-auto">
      <div class="prompt">Where would you like to go?</div>
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
