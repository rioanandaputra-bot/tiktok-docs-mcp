import { API_OPERATION_TYPE_MAP } from "../api";
import { ClientConfiguration } from "./config";
import { createApiInstance } from "./create-api-instance";
import { AccessToken } from "./token";

export class TikTokShopNodeApiClient {
  readonly config?: ClientConfiguration;
  readonly api: API_OPERATION_TYPE_MAP;

  constructor({ config }: { config?: ClientConfiguration }) {
    this.config = config;
    const { api } = createApiInstance(this);
    this.api = api;
  }
}