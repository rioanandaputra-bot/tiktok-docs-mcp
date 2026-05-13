import { createTransRequestOptionsInterceptor } from './create-trans-request-options';
import { createCallApiMap } from './create-call-api-map';
import { TikTokShopNodeApiClient } from './client';

const basePath = 'https://open-api.tiktokglobalshop.com';

export const createApiInstance = (client: TikTokShopNodeApiClient) => {
  const path = client.config?.basePath || basePath;

  const interceptor = createTransRequestOptionsInterceptor(client);

  const apiInstanceGroup = createCallApiMap(path, interceptor);

  return {
    api: apiInstanceGroup,
  };
};
