export interface Message {
  type: "user" | "ai" | "error" | "loading";
  content: string;
}
