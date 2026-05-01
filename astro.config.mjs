import { defineConfig } from 'astro/config';

export default defineConfig({
  output: 'static',
  site: 'https://DC4869.github.io',
  image: {
    service: {
      entrypoint: 'astro/services/sharp',
      config: {
        mode: 'compile'
      }
    }
  },
});