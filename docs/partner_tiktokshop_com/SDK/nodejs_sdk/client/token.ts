import { ClientConfiguration } from "./config";
import localVarRequest from "request";

const auth_host = "https://auth.tiktok-shops.com";

const refresh_token_path = "/api/v2/token/refresh";
const get_access_token_path = "/api/v2/token/get";

const grant_type = "authorized_code";

export type AccessTokenProps = {
  access_token: string;
  refresh_token?: string;
  config?: ClientConfiguration;
};

export enum UserType {
  Seller = 0,
  Creator = 1,
}

export type BaseResponse<T> = {
  /**
   * The success or failure status code returned in API response.
   */
  code?: number;
  data?: T;
  /**
   * The success or failure messages returned in API response. Reasons of failure will be described in the message.
   */
  message?: string;
  /**
   * Request log.
   */
  requestId?: string;
};

export type TokenResponse = {
  /**
   * @description User access token needed to make calls to TikTok Shop Open API endpoints
   */
  access_token: string;
  /**
   * @description Expiration timestamp for access token, with default expiration time set to seven days. The Unix timestamp represents the date and time the access token will expire.
   */
  access_token_expire_in?: number;
  /**
   * @description A token to refresh the access token
   */
  refresh_token: string;
  /**
   * @description Expiration timestamp for refresh token. The Unix timestamp represents the date and time the refresh token will expire.
   */
  refresh_token_expire_in?: number;
  /**
   * @description The ID to help you identify a TikTok Shop seller in your platform
   */
  open_id?: string;
  /**
   * @description The name of the seller you are authorizing for your app
   */
  seller_name?: string;
  /**
   * @description The region where the seller is based
   */
  seller_base_region?: string;
  /**
   * @description Type of user, with possible values:
   * @enum 0 Seller
   * @enum 1 Creator
   */
  user_type?: UserType;
  /**
   * @description ID to track the API request
   */
  request_id?: string;
};

class AccessToken {
  access_token: string;
  refresh_token?: string;
  config?: ClientConfiguration;
  constructor({ access_token, refresh_token, config }: AccessTokenProps) {
    this.access_token = access_token;
    this.refresh_token = refresh_token;
    this.config = config;
  }

  async refreshToken(props: { refresh_token?: string; auto_filled?: boolean }) {
    const { refresh_token: _refresh_token, auto_filled = false } = props;

    const path = auth_host + refresh_token_path;
    // 请求逻辑
    const app_key =
      this.config?.app_key || ClientConfiguration.globalConfig.app_key;
    const app_secret =
      this.config?.app_secret || ClientConfiguration.globalConfig.app_secret;
    const refresh_token = _refresh_token || this.refresh_token;

    if (!app_key) {
      throw new Error("app_key is required");
    }
    if (!app_secret) {
      throw new Error("app_secret is required");
    }
    if (!refresh_token) {
      throw new Error("refresh_token is required");
    }
    const qs = {
      grant_type,
      refresh_token,
      app_key,
      app_secret,
    };

    const options: localVarRequest.Options = {
      method: "GET",
      url: path,
      qs,
      useQuerystring: true,
    };
    return new Promise<{
      response: localVarRequest.Response;
      body: BaseResponse<TokenResponse>;
    }>((resolve, reject) => {
      localVarRequest(
        options,
        (error, response, body: BaseResponse<TokenResponse>) => {
          if (error) {
            reject(error);
          }

          if (auto_filled) {
            if (body.data?.access_token)
              this.access_token = body.data?.access_token;
            if (body.data?.refresh_token)
              this.refresh_token = body.data?.refresh_token;
          }

          resolve({
            response,
            body,
          });
        }
      );
    });
  }

  async getAccessToken(props: { auth_code: string; auto_filled?: boolean }) {
    const { auth_code, auto_filled = false } = props;

    const path = auth_host + get_access_token_path;
    // 请求逻辑
    const app_key =
      this.config?.app_key || ClientConfiguration.globalConfig.app_key;
    const app_secret =
      this.config?.app_secret || ClientConfiguration.globalConfig.app_secret;

    if (!app_key) {
      throw new Error("app_key is required");
    }
    if (!app_secret) {
      throw new Error("app_secret is required");
    }
    if (!auth_code) {
      throw new Error("auth_code is required");
    }

    const qs = {
      grant_type,
      auth_code,
      app_key,
      app_secret,
    };

    const options: localVarRequest.Options = {
      method: "GET",
      url: path,
      qs,
      useQuerystring: true,
    };
    return new Promise<{
      response: localVarRequest.Response;
      body: BaseResponse<TokenResponse>;
    }>((resolve, reject) => {
      localVarRequest(
        options,
        (error, response, body: BaseResponse<TokenResponse>) => {
          if (error) {
            reject(error);
          }

          if (auto_filled) {
            if (body.data?.access_token)
              this.access_token = body.data?.access_token;
            if (body.data?.refresh_token)
              this.refresh_token = body.data?.refresh_token;
          }

          resolve({
            response,
            body,
          });
        }
      );
    });
  }
}

class AccessTokenBuilder {
  static build(
    access_token: string,
    refresh_token?: string,
    config?: ClientConfiguration
  ) {
    return new AccessToken({
      access_token,
      refresh_token,
      config,
    });
  }
}

class AccessTokenTool {
  static async refreshToken(
    refresh_token: string,
    app_key?: string,
    app_secret?: string
  ) {
    let _app_key = app_key || ClientConfiguration.globalConfig.app_key;
    let _app_secret = app_secret || ClientConfiguration.globalConfig.app_secret;
    if (!_app_key) {
      throw new Error("app_key is required");
    }
    if (!_app_secret) {
      throw new Error("app_secret is required");
    }
    if (!refresh_token) {
      throw new Error("refresh_token is required");
    }

    const path = auth_host + refresh_token_path;
    // 请求逻辑
    const qs = {
      grant_type,
      refresh_token,
      app_key: _app_key,
      app_secret: _app_secret,
    };

    const options: localVarRequest.Options = {
      method: "GET",
      url: path,
      qs,
      useQuerystring: true,
    };

    return new Promise<{
      response: localVarRequest.Response;
      body: BaseResponse<TokenResponse>;
    }>((resolve, reject) => {
      localVarRequest(
        options,
        (error, response, body: BaseResponse<TokenResponse>) => {
          if (error) {
            reject(error);
          }

          resolve({
            response,
            body,
          });
        }
      );
    });
  }

  static async getAccessToken(
    auth_code: string,
    app_key?: string,
    app_secret?: string
  ) {
    let _app_key = app_key || ClientConfiguration.globalConfig.app_key;
    let _app_secret = app_secret || ClientConfiguration.globalConfig.app_secret;

    if (!_app_key) {
      throw new Error("app_key is required");
    }
    if (!_app_secret) {
      throw new Error("app_secret is required");
    }
    if (!auth_code) {
      throw new Error("auth_code is required");
    }

    const path = auth_host + get_access_token_path;
    const qs = {
      grant_type,
      auth_code,
      app_key: _app_key,
      app_secret: _app_secret,
    };

    const options: localVarRequest.Options = {
      method: "GET",
      url: path,
      qs,
      useQuerystring: true,
    };

    return new Promise<{
      response: localVarRequest.Response;
      body: BaseResponse<TokenResponse>;
    }>((resolve, reject) => {
      localVarRequest(
        options,
        (error, response, body: BaseResponse<TokenResponse>) => {
          if (error) {
            reject(error);
          }

          resolve({
            response,
            body,
          });
        }
      );
    });
  }
}

export { AccessTokenBuilder, AccessTokenTool, AccessToken };