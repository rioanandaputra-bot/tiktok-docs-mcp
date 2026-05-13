import localVarRequest from "request";
import { Interceptor } from "../model/models";
import { generateSign } from "../utils/generate-sign";
import { TikTokShopNodeApiClient } from "./client";
import { ClientConfiguration } from "./config";

export const createTransRequestOptionsInterceptor =
  (client: TikTokShopNodeApiClient): Interceptor =>
  async (option: localVarRequest.Options) => {
    const clientConfig = client.config;

    const app_key =
      clientConfig?.app_key || ClientConfiguration.globalConfig.app_key;
    const app_secret =
      clientConfig?.app_secret || ClientConfiguration.globalConfig.app_secret;
    const timestamp = Math.floor(Date.now() / 1000);

    if (!app_key) {
      throw new Error("app_key is required");
    }
    if (!app_secret) {
      throw new Error("app_secret is required");
    }

    option.qs = {
      timestamp,
      app_key,
      ...option.qs,
    };

    if (option.qs) {
      const newQs: Record<string, any> = {};
      for (const key in option.qs) {
        if (Object.prototype.hasOwnProperty.call(option.qs, key)) {
          const element = option.qs[key];
          if (Array.isArray(element)) {
            newQs[key] = element.join(",");
          } else {
            newQs[key] = element;
          }
        }
      }
      option.qs = newQs;
    }

    option.headers = {
      "Content-Type": "application/json",
      'User-Agent': 'sdk_node/1.0.0',
      // "x-tts-access-token": access_token,
      ...option.headers,
    };

    option.qs["sign"] = generateSign(option, app_secret);

    return;
  };