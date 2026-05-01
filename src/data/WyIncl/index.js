import MCPol from './MCPol.json';

const meta = {
  id: 'WyIncl',
  name: 'Wy inclusive Analysis',
  description: 'ATLAS Run2 inclusive Wy leptonic differential measurement',
};

const subpages = [
  MCPol,
];

export default {
  ...meta,
  subpages,
};
