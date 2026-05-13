import { API_OPERATION_TYPE_MAP, API_OBJECT, API_ENUM } from "../api";
import { ClientConfiguration } from "./config";

const createCallApiMap = (
  basePath?: string,
  interceptor?: Function
): API_OPERATION_TYPE_MAP => {
  // @ts-ignore
  const callApiMap: API_OPERATION_TYPE_MAP = {};

  for (const apiClientName in API_OBJECT) {
    if (Object.prototype.hasOwnProperty.call(API_OBJECT, apiClientName)) {
      const ApiClient = API_OBJECT[
        apiClientName as keyof typeof API_OBJECT
      ] as (typeof API_OBJECT)[API_ENUM];
      const apiClient = new ApiClient(basePath);
      if (interceptor) apiClient.addInterceptor(interceptor as any);
      //@ts-ignore
      callApiMap[apiClientName] = apiClient;
    }
  }

  return callApiMap;
};

export { createCallApiMap };