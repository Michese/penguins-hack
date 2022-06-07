import { Api } from '@/api/Api';

export class DataProjectApi extends Api {
    /**
     * Залогиниться
     * @param {FormData} data
     * @returns {Promise<{ result: number }>}
     */
    static async compute(data) {
        return this.get(`/api/compute`, data);
    }
}