# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:41:39 2021

@author: shengrihui
"""

import requests
from lxml import etree

url='https://sanhe.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0030-896e-227a-12a125a87564&ClickID=3'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

page_text=requests.get(url=url,headers=header).text
#print(page_text)

#实例化etree对象
tree=etree.HTML(page_text)
#print(tree)

def test01():
    #<h3 title="北欧上六小八中，正规两室一厅，总价125万" class="property-content-title-name" style="max-width:501px;" data-v-94adac58="">北欧上六小八中，正规两室一厅，总价125万</h3>
    r=tree.xpath('//h3[@class="property-content-title-name"]/text()')
    
    for i in r:
        print(i)
        
def test02():
    '''
    <div tongji_tag="fcpc_ersflist_gzcount" class="property" data-v-94adac58="" data-v-bc00cb90=""><a href="https://lf.58.com/ershoufang/45885373014153x.shtml?auction=200&amp;hpType=60&amp;entry=102&amp;position=0&amp;kwtype=filter&amp;now_time=1618573989&amp;typecode=200&amp;lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3Dszq_uB3draOWUvYfugF1pAqduh78uztYPH93PHnLn1TQPjDdnL980v6YUykKuadbn19dn1KhradbrHEdsHELuWnVmHTYraYknhNvP1PBPAE1uADKPWmvPHnkPW03nj0zPj9KTHDOPHDzrjmkPWD3PHDvPWnKnWnLnjTKnWnLnjTKnikQnkDLP1mKnHmQrjNLn1b3rHnvnkDdTNujgYRHw-qniRPNgdKjTHDKnEDKsHDKTHD1rjcOnHTLnjEzPHbOPWbknWEKP9DKnE7hrAnduWcQmidBuyc1sHE1PjEVryE3mBdWPHNkuWE3mHmznHDKnHn3nWbQnj0kPjEknWNLnHcvPTDQn19zrHDkP1TYn1TQrHTLrHm3TEDKTEDKsEDKTED3nbRKPW7KriYvPDRasHEzEHnVrDRjnaYQEYmOnHEdwNDdnHEKnWcQsWDOPa3Qn1b8nHTYTHTKnTDKnikQnk7exEDQnjT1n9DQnjTQrjn3TyNQmvuWn1nYsH76rAEVPA7Wnzd6njKBsHm3n1whnHnvm1K6mkDKnTDKTHTKP10zsjcvnjcOsjcvnHTdTHDKUMR_UTDQPvPhrymLnAPBPjwhPW-h&amp;spread=filtersearch&amp;from=from_esf_List_search&amp;index=0" data-action="esf_list" target="_blank" data-trace="{&quot;exposure&quot;:{&quot;entry_source&quot;:&quot;Anjuke_Hp_View&quot;,&quot;from_id&quot;:&quot;1&quot;,&quot;project_id&quot;:&quot;200&quot;,&quot;source_type&quot;:1,&quot;hp_type&quot;:&quot;2&quot;,&quot;ax_type&quot;:&quot;1&quot;,&quot;search_type&quot;:&quot;filter&quot;,&quot;vpid&quot;:&quot;45885373014153&quot;,&quot;v&quot;:&quot;2.0&quot;,&quot;hp_page&quot;:&quot;Anjuke_Hp_View&quot;,&quot;channel&quot;:&quot;1&quot;,&quot;community_id&quot;:&quot;102381770&quot;,&quot;area_id&quot;:&quot;35353&quot;,&quot;esf_id&quot;:45885373014153,&quot;isauction&quot;:200,&quot;pos&quot;:0,&quot;trading_area_ids&quot;:0,&quot;found&quot;:0,&quot;prop_expire&quot;:0,&quot;entry&quot;:0,&quot;tradeType&quot;:&quot;2&quot;,&quot;esf_list&quot;:1,&quot;broker_id&quot;:&quot;200457646&quot;}}" data-cp="{&quot;broker_id&quot;:&quot;200457646&quot;}" data-lego="{&quot;entity_id&quot;:&quot;1951286061851663&quot;,&quot;tid&quot;:&quot;e1cfc334-1a8d-4ac3-a00b-6834f136c0ac&quot;}" class="property-ex" data-v-94adac58="" data-exposure="true"><div class="property-image" data-v-94adac58=""><img alt="" src="https://pic1.ajkimg.com/display/58ajk/b67da402ab0eff392d71e379e4415b2f/640x420c.jpg?t=1" class="lazy-img cover" data-v-28819723="" data-v-94adac58="" data-src="https://pic1.ajkimg.com/display/58ajk/b67da402ab0eff392d71e379e4415b2f/640x420c.jpg?t=1" lazy="loaded"> <!----> <span id="main-0" class="property-image-vr" data-v-94adac58=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 370 370" width="370" height="370" preserveAspectRatio="xMidYMid meet" style="width: 100%; height: 100%; transform: translate3d(0px, 0px, 0px);"><defs><clipPath id="__lottie_element_2"><rect width="370" height="370" x="0" y="0"></rect></clipPath><clipPath id="__lottie_element_4"><path d="M0,0 L300,0 L300,300 L0,300z"></path></clipPath></defs><g clip-path="url(#__lottie_element_2)"><g transform="matrix(1.2239700555801392,0,0,1.2239700555801392,185,169.00025939941406)" opacity="0.5" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,-0.27300000190734863,13.72700023651123)"><path fill="rgb(0,0,0)" fill-opacity="1" d=" M0,-150 C82.78500366210938,-150 150,-82.78500366210938 150,0 C150,82.78500366210938 82.78500366210938,150 0,150 C-82.78500366210938,150 -150,82.78500366210938 -150,0 C-150,-82.78500366210938 -82.78500366210938,-150 0,-150z"></path></g></g><g clip-path="url(#__lottie_element_4)" transform="matrix(1,0,0,1,35,35)" opacity="1" style="display: block;"><g transform="matrix(1,0,0,1,145,145)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,0,0)"><path stroke-linecap="butt" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="4" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="13.599" d="M0 0"></path></g><g opacity="1" transform="matrix(1,0,0,1,-17.826000213623047,-17.326000213623047)"><path fill="rgb(255,255,255)" fill-opacity="0" d=" M69,-69 C69,-69 69,69 69,69 C69,69 -69,69 -69,69 C-69,69 -69,-69 -69,-69 C-69,-69 69,-69 69,-69z"></path><path stroke-linecap="butt" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="4" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="12" d=" M69,-69 C69,-69 69,69 69,69 C69,69 -69,69 -69,69 C-69,69 -69,-69 -69,-69 C-69,-69 69,-69 69,-69z"></path></g><g opacity="1" transform="matrix(1,0,0,1,0,0)"><path fill="rgb(255,255,255)" fill-opacity="0" d=" M-87,-86.5 C-87,-86.5 -48,-47.5 -48,-47.5"></path><path stroke-linecap="butt" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="4" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="12" d=" M-87,-86.5 C-87,-86.5 -48,-47.5 -48,-47.5"></path></g></g><g transform="matrix(-1,0,0,-1,149.34799194335938,150.34799194335938)" opacity="1" style="display: block;"><g opacity="1" transform="matrix(1,0,0,1,-18.013999938964844,-17.85700035095215)"><path fill="rgb(255,255,255)" fill-opacity="0.3" d=" M69,-69 C69,-69 69,69 69,69 C69,69 -69,69 -69,69 C-69,69 -69,-69 -69,-69 C-69,-69 69,-69 69,-69z"></path><path stroke-linecap="butt" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="4" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="12" d=" M69,-69 C69,-69 69,69 69,69 C69,69 -69,69 -69,69 C-69,69 -69,-69 -69,-69 C-69,-69 69,-69 69,-69z"></path></g><g opacity="1" transform="matrix(1,0,0,1,0,0)"><path fill="rgb(255,255,255)" fill-opacity="1" d=" M-87,-86.5 C-87,-86.5 -48,-47.5 -48,-47.5"></path><path stroke-linecap="butt" stroke-linejoin="miter" fill-opacity="0" stroke-miterlimit="4" stroke="rgb(255,255,255)" stroke-opacity="1" stroke-width="12" d=" M-87,-86.5 C-87,-86.5 -48,-47.5 -48,-47.5"></path></g></g></g></g></svg></span></div> <div class="property-content" data-v-94adac58=""><div class="property-content-detail" data-v-94adac58=""><div class="property-content-title" data-v-94adac58=""><h3 title="MTOWN严选 130平大三居 东南北 小区  户型 急售" class="property-content-title-name" style="max-width:435px;" data-v-94adac58="">MTOWN严选 130平大三居 东南北 小区  户型 急售</h3> <img src="https://pages.anjukestatic.com/usersite/site/img/broker_detail/esf_list_icon_anxuan_pinzhihaofang_gold4@2x.png" class="property-content-title-anxuan" style="width:104px;height:24px;" data-v-94adac58="">  <span class="property-content-title-othertag-ad" data-v-94adac58="">广告</span></div> <section data-v-94adac58=""><div class="property-content-info" data-v-94adac58=""><p class="property-content-info-text property-content-info-attribute" data-v-94adac58=""><span data-v-94adac58="">3</span> <span data-v-94adac58="">室</span> <span data-v-94adac58="">2</span> <span data-v-94adac58="">厅</span> <span data-v-94adac58="">2</span> <span data-v-94adac58="">卫</span></p> <p class="property-content-info-text" data-v-94adac58="">
                            130.8㎡
                        </p> <p class="property-content-info-text" data-v-94adac58="">南北</p> <p class="property-content-info-text" data-v-94adac58="">
                            高层(共11层)
                        </p> <p class="property-content-info-text" data-v-94adac58="">
                            2008年建造
                        </p></div> <div class="property-content-info property-content-info-comm" data-v-94adac58=""><p class="property-content-info-comm-name" data-v-94adac58="">星河皓月</p> <p class="property-content-info-comm-address" data-v-94adac58=""><span data-v-94adac58="">燕郊镇</span><span data-v-94adac58="">燕郊城区</span><span data-v-94adac58="">燕顺路,近燕兴街</span></p></div> <div class="property-content-info" data-v-94adac58=""><span class="property-content-info-tag" data-v-94adac58="">满五唯一</span><span class="property-content-info-tag" data-v-94adac58="">新上</span></div></section> <div class="property-extra-wrap" data-v-94adac58=""><div class="property-extra" data-v-94adac58=""><div class="property-extra-photo" data-v-94adac58=""><img alt="" src="https://pic1.ajkimg.com/display/7bc8117bca2b43fbf455262007c18e89/100x133.jpg" class="lazy-img cover" data-v-28819723="" data-v-94adac58="" data-src="https://pic1.ajkimg.com/display/7bc8117bca2b43fbf455262007c18e89/100x133.jpg" lazy="loaded"></div> <span class="property-extra-text" data-v-94adac58="">乌红杰</span> <!----> <span class="property-extra-text" data-v-94adac58="">4.6分</span> <span class="property-extra-text" data-v-94adac58="">专注房产</span></div> <!----></div></div> <div class="property-price" data-v-94adac58=""><p class="property-price-total" data-v-94adac58=""><span class="property-price-total-num" data-v-94adac58="">285</span> <span class="property-price-total-text" data-v-94adac58="">万</span></p> <p class="property-price-average" data-v-94adac58="">21786元/㎡</p></div></div></a></div>
    
    <p class="property-price-total" data-v-94adac58=""><span class="property-price-total-num" data-v-94adac58="">285</span> <span class="property-price-total-text" data-v-94adac58="">万</span></p>
    <span class="property-price-total-num" data-v-94adac58="">285</span>
    
    '''
    div_list=tree.xpath('//div[@class="property"]')
    #print(div_list)
    #print(len(div_list))
    
    fp=open('02 58.txt','w',encoding='utf-8')
    for div in div_list:
        #局部xpath需要加点
        title=div.xpath('.//h3[@class="property-content-title-name"]/text()')
        #print(title)
        
        price=div.xpath('.//p[@class="property-price-total"]//text()')
        print(price)
        fp.writelines(title)
        fp.write('\t')
        fp.write(''.join([price[0],price[2]]))
        fp.write('\n')

    fp.close()
#test01()
test02()
