class GlobalClientConfiguration {
  static app_key?: string;
  static app_secret?: string;
  static basePath?: string;
}
class ClientConfiguration {
  app_key?: string;
  app_secret?: string;
  basePath?: string;

  static globalConfig = GlobalClientConfiguration;

  constructor(
    app_key?: string,
    app_secret?: string,
    basePath?: string,
  ) {
    this.app_key = app_key;
    this.app_secret = app_secret;
    this.basePath = basePath;
  }
  static createConfig() {
    const client = new ClientConfiguration();

    const configObject = {
      setAppKey(app_key: string) {
        client.app_key = app_key;
        return configObject;
      },
      setAppSecret(app_secret: string) {
        client.app_secret = app_secret;
        return configObject;
      },
      setBasePath(basePath: string) {
        client.basePath = basePath;
        return configObject;
      },
      build() {
        return client;
      },
    };
    return configObject;
  }
}

export { ClientConfiguration };