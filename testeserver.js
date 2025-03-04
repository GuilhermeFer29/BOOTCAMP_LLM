import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    vus: 1000,  // Número de usuários virtuais
    duration: '30s',  // Duração do teste
};

export default function () {
    let res = http.get('https://dash.serverhome.top/');
    check(res, {
        'status é 200': (r) => r.status === 200,
        'tempo de resposta < 500ms': (r) => r.timings.duration < 500,
    });
    sleep(1);  // Pausa de 1 segundo entre as requisições
}
