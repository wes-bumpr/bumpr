import { TimingButton } from "./TimingButton.jsx";

export function NowLater() {
  return (
    <div class="col-auto">
      <h1 class="prompt">
        Are you booking this ride for...
      </h1>
      <div class="timingbuttons">
        <TimingButton />
      </div>
    </div>
  );
}
