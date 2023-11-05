export function AddressTo({
  toText,
  searchResultsTo,
  autocompleteTo,
  addressSelectTo,
  sToAddress
}) {

  return (
    <div class="col-auto">
      <div class="prompt">Where would you like to go?</div>
      <div class="selected_address">{sToAddress}</div>
      <div class="addressholder">
        <input
          type="text"
          value={toText}
          onChange={(e) => autocompleteTo(e.target.value)}
        ></input>
        <div class="list-group addressresults">
          {searchResultsTo.map((item) => (
            <button
              href=""
              class="list-group-item list-group-item-action"
              aria-current="true"
              onClick={(e)=>addressSelectTo(e.target.innerText, item.x, item.y)}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
