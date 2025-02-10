import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import App from "./App.vue";

// Import styles
import "vant/lib/index.css";
import "./styles/index.scss";

// Import Vant
import Vant from "vant";

// Create app
const app = createApp(App);

// Create and use Pinia before mounting
const pinia = createPinia();
app.use(pinia);

// Use other plugins
app.use(router);
app.use(Vant);

app.mount("#app");
