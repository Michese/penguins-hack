import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueJsx()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '~bootstrap': 'bootstrap',
    }
  },
  preview: {
    host: '0.0.0.0',
    port: 3000,
    proxy: {
      '/api': {
        // target: 'http://172.16.238.2:5000',
        target: 'http://localhost:5000',
        secure: false,
        changeOrigin: true,
      },
    }
  },
  server: {
    port: 3000,
    host: '0.0.0.0',
    proxy: {
      '^/api': {
        // target: 'http://172.16.238.2:5000',
        target: 'http://localhost:5000',
        secure: false,
        changeOrigin: true,
      },
    }
  }
})
