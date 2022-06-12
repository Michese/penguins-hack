import {Api} from '@/api/Api';

export class DataProjectApi extends Api {
    /**
     * Залогиниться
     * @returns {Promise<{ result: number }>}
     */
    static async user() {
        return this.get(`/api/user`);
    }

    /**
     * Залогиниться
     * @returns {Promise}
     */
    static async classmates() {
        return this.get(`/api/classmates`);
    }

    /**
     * Залогиниться
     * @returns {Promise}
     */
    static async telegramm() {
        return this.get(`/api/telegramm`);
    }
    /**
     * Залогиниться
     * @returns {Promise}
     */
    static async vk() {
        return this.get(`/api/vk`);
    }
}