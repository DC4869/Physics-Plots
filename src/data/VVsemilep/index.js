import MCPol from './MCPol.json';
import modeling from './modeling.json';

const meta = {
  id: 'VVsemilep',
  name: 'VV semilep Analysis',
  description: 'ATLAS Run3 inclusive VV semileptonic differential measurement',
};

const subpages = [
  MCPol,
  modeling,
];

export default {
  ...meta,
  subpages,
};
