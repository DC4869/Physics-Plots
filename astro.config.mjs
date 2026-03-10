import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  site: 'https://plots.milescb.com',
  image: {
    service: {
      entrypoint: 'astro/services/sharp',
      config: {
        mode: 'compile'
      }
    }
  },
});