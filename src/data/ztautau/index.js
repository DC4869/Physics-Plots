import controlRegions from './control-regions.json';
import background from './background.json';
import modelingWithW from './modeling-with-w.json';
import systematics from './systematics.json';
import fits from './fits.json';
import valBoomSx from './val-boom-sx.json';

const meta = {
  id: 'ztautau',
  name: 'Ztautau Analysis',
  description: 'Search for CP Violation in the Z to tau-tau system',
};

const subpages = [
  controlRegions,
  background,
  modelingWithW,
  systematics,
  fits,
  valBoomSx,
];

export default {
  ...meta,
  subpages,
};
