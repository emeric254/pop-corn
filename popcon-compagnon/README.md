# popcon-compagnon

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

### Build a container ("docker") image for Production deployments

```sh
npm run podman

# ~ or if you only got docker :
# npm run docker
```

Now you can start a container :

```sh
podman run --rm -p 8080:8080 localhost/popcon-compagnom:latest
# you can replace podman by docker if needed
```

Modify the port (left part) as you wish.

Replace the `./public/donnees/` path to the folder you want to mount inside the container.

```sh
podman run --rm -p 8080:8080 -v ./public/donnees/:/usr/share/nginx/html/donnees/ localhost/popcon-compagnon:latest
```
