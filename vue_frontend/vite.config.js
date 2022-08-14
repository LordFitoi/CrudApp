const { resolve } = require('path');
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const staticPath = '../app/static/vue/';
const appsEntries = {
    contacts: resolve('./src/app/main.js'),
}

export default defineConfig({
    root: resolve(staticPath),
    base: '/static/',
    plugins: [vue()],
    build: {
        outDir: resolve(staticPath),
        manifest: true,
        emptyOutDir: true,
        rollupOptions: {
            output: {
                entryFileNames: `[name].js`,
                chunkFileNames: `[name].js`,
                assetFileNames: `[name].[ext]`
            },
            input: appsEntries
        },
    },
    resolve:{
        alias: {
            'vue': 'vue/dist/vue.esm-bundler.js',
            '@' : resolve(__dirname, '../app/static') }
    },
})