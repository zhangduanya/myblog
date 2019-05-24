#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-5-17 11:02
# @Author  : zhdya@zhdya.cn
# @File    : test.py

import base64
import hashlib
import hmac
import time
import requests
import json

# list = [ins-rb67q9b7,ins-1ort8z45ins-kv1ohcrl,ins-ag6stthj,ins-4lrn8e4n,ins-d5lm9dsx,ins-085z5k4r,ins-4exob31f,ins-0gsag0uh,ins-93njuduv,ins-ggqirmfj,ins-pgdajx2l,ins-9kdedesj,ins-3g69vff3,ins-llprnvn1,ins-kv2ukttt,ins-rjlaui9z,ins-jakw6h9p,ins-2fero3u1,ins-qsoycp49,ins-0glizc3v,ins-fkwqbvmx,ins-hvk0s9t1,ins-cjpki4b1,ins-4mli6zu3,ins-nwahn30j,ins-lf9ruhab,ins-2g2mvb7r,ins-ci4vckq5,ins-oc5io3kd,ins-n18a3lrd,ins-nq5l7jot,ins-irsi5693,ins-8fwct8hx,ins-ntnnsbih,ins-9fxqsrwh,ins-8ot3tqi7,ins-qr6jbsll,ins-fm4gwjfl,ins-6pgrkin9,ins-kz7kd087,ins-2fuaykkh,ins-6ot01jux,ins-qwmgmskr,ins-0ohmhlfx,ins-0o758odl,ins-hwpug55z,ins-bbyq4tgl,ins-4zf6cwqx,ins-l2g0chad,ins-rza6hrsd,ins-juij1g3l,ins-1zkh6fph,ins-dlc6znl5,ins-pcwho50r,ins-l20jasln,ins-r0huxx7n,ins-6tx56eat,ins-mann69k1,ins-0ztmkged,ins-hvbc5yyt,ins-iv3x9ukp,ins-o9l8v8ip,ins-5ewx2v0p,ins-854fbecv,ins-p8fhs171,ins-q48vm5ib,ins-nwbffijz,ins-ltsg62ix,ins-bj5505c7,ins-8kayodwh,ins-nechnkjp,ins-56330n7v,ins-odnb7zj9,ins-p1k3qvhf,ins-ndbef99r,ins-cj7ly8sl,ins-acgks6nh,ins-6p7yc1xn,ins-abr5puar,ins-g8vy3jlx,ins-p49rmv4x,ins-bzvq6aht,ins-caysjalh,ins-h4vflqx3,ins-0sej16xz,ins-kpxvzls7,ins-n9ochmkv,ins-hl8cf613,ins-9fornbb7,ins-46jdeald,ins-gxgl7jc7,ins-gnvdhn57,ins-klzxqrhl,ins-kfbkx4ct,ins-6d74yep1,ins-as7s610t,ins-nogyiubz,ins-hnfplea7,ins-8l2rzl0p,ins-rnicpg8d,ins-ib0um3sd,ins-e6wbpggd,ins-2evivdmx,ins-l9vyvq5n,ins-b067gvet,ins-ooeiia8b,ins-5dhee8w1,ins-3ymqhtzh,ins-30cw0bmp,ins-102i03an,ins-1g5onjhd,ins-8vngyz3f,ins-des7ipxj,ins-0gc163vl,ins-gsa29yfd,ins-0ophd2rx,ins-g1vgfnsx,ins-6xgdvhcf,ins-7tx16mw5,ins-2870tqsr,ins-q0hvys5f,ins-cbi8u2mf,ins-mtbmflvn,ins-2gm0l5cb,ins-4mcmno6l,ins-1buuslkx,ins-gnvcq2tf,ins-c7v92l3h,ins-804lwosr,ins-fslhuiwd,ins-a4bq0621,ins-odudmrn3,ins-nkfki2bp,ins-exzhj3b9,ins-qjk0q70r,ins-4qi0dvgj,ins-mpdxvn7v,ins-cahipkml,ins-0l18hb5t,ins-2ze4w4vb,ins-7gn66qbt,ins-igjvbdnv,ins-o8muneud,ins-8ok8nnj7,ins-ey0l3ywb,ins-fhwdndfr,ins-9kk316ld,ins-bjxg9i81,ins-0s8jhbcd,ins-eloh25f3,ins-qr48r6yz,ins-95bftolr,ins-eab4zaat,ins-lxav6s4j,ins-8thpjlup,ins-lj9j0wbv,ins-7a9vpotr,ins-4xxhjabp,ins-7ddxqcuf,ins-424pdne5,ins-7s6pbwud,ins-n5o4d9mx,ins-6czr7v7r,ins-cj5zdcat,ins-hsdrecmh,ins-a8rvxqcn,ins-0k31ja0z,ins-po75btcz,ins-p8ntgpxn,ins-3jtxo9gv,ins-e5f20tmr,ins-lmeod5c5,ins-hjw2hiox,ins-bzwvj8eh,ins-1c3vodqj,ins-gxh7kl29,ins-bo535bux,ins-inx89pc5,ins-og0md3rj,ins-oxavmq11,ins-4enr8h6r,ins-n5dzpm1t,ins-5n1fb7yj,ins-ps4mawub,ins-kfqjxtv3,ins-0p02hvkd,ins-j3vzrobp,ins-gplo4h7p,ins-0glfjnil,ins-pjz5awir,ins-7sr8k5d3,ins-9kdgqbr7,ins-5mthdhrb,ins-hz9zvj8p,ins-onyl69t3,ins-8rz86hjf,ins-5xmivo93,ins-fxihplvn,ins-dywdtu25,ins-asagp6a3,ins-6u5ms7qh,ins-baq4aixb,ins-0zmb6x9n,ins-jc18qp8j,ins-9s81b401,ins-jvawaz65,ins-m95pxetl,ins-qcohjxcx,ins-3berhqod,ins-4egm3tm5,ins-n1r4y2ct,ins-hs2t0k2p,ins-jzjzlmzz,ins-prolvhet,ins-88iwdtu7,ins-pgaywuyz,ins-10k9f7xl,ins-mqfoc2qr,ins-g4vvr9nr,ins-1swruexx,ins-gpnazk2p,ins-2klrx09b,ins-p7vdlomb,ins-dmmsxfur,ins-f4wo6wj1,ins-9h5lenph,ins-2ohq56gx,ins-5deo71ql,ins-a363s9z5,ins-69xwy7il,ins-eqc4zdrh,ins-cmlp0bqh,ins-hnenwqdp,ins-q01fq43l,ins-33sqmwmn,ins-n1i5rgnf,ins-4ecq04rl,ins-66l01hqj,ins-deiulrib,ins-aewbq4x9]
secret_id = "AKIDdDd1IRIBmCQTKvGkwwkMm143sVwAbRVx"
secret_key = "a0FIArNsIXlneTAqKcxHVYO2d2LSWCxW"

timeStramp = int(time.time())
print(timeStramp)

def get_string_to_sign(method, endpoint, params):
    s = method + endpoint + "/?"
    query_str = "&".join("%s=%s" % (k, params[k]) for k in sorted(params))
    return s + query_str

def sign_str(key, s, method):
    hmac_str = hmac.new(key.encode("utf8"), s.encode("utf8"), method).digest()
    return base64.b64encode(hmac_str)

if __name__ == '__main__':
    endpoint = "cvm.tencentcloudapi.com"
    data = {
        'Action' : 'DescribeInstances',       ##查看实例信息的接口
        # 'Action' : 'RebootInstances',       ##重启的接口
        'InstanceIds.0' : 'ins-oxacjavi',
        # 'ForceReboot' : 'FALSE',    ##重启的信息
        'Limit' : 20,     ##实例信息
        'Nonce' : 11886,
        'Offset' : 0,     ##实例信息
        'Region' : 'ap-guangzhou',
        'SecretId' : secret_id,
        'Timestamp' : timeStramp, # int(time.time())
        'Version': '2017-03-12'
    }
    s = get_string_to_sign("GET", endpoint, data)
    data["Signature"] = sign_str(secret_key, s, hashlib.sha1)
    print(data["Signature"])
    # 此处会实际调用，成功后可能产生计费
    resp = requests.get("https://" + endpoint, params=data)
    print(resp.url)
    print(resp.json())
