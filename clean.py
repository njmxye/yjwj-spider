import json
from yjwjrank import getname,getrecord,hint,time_shift,nameolding
def main():
    name = getname()
    oldname=nameolding(name)
    hint(name)
    data_json=getrecord(name)
    game_modes = {
            0: "全部",
            1: "天选单排",
            2: "天选三排",
            3: "无尽试炼",
            4: "天人单排",
            5: "天人三排",
            6: "匹配单排",
            7: "匹配三排",
            9: "匹配双排",
            10: "无尽试炼双排",
            11: "无尽试炼三排",
            12: "天选双排",
            13: "天人双排"
        }

    scenes = {
            1: "聚窟洲",
            2: "火罗国",
            3: "龙隐洞天"
        }
    heros = {
        1000001:'土御门胡桃',
1000003:'宁红夜',
1000004:'迦南',
1000005:'特木尔',
1000006:'季沧海',
1000007:'天海',
1000009:'妖刀姬',
1000010:'崔三娘',
1000011:'岳山',
1000013:'无尘',
1000015:'顾清寒',
1000016:'武田信忠',
1000017:'殷紫萍',
1000018:'沈妙',
1000020:'1000020',
1000021:'1000021',
1000022:'1000022',
1000023:'1000023',
1000024:'1000024'
    }

    data = json.loads(data_json)

    def clean_data(data, game_modes, scenes):
        cleaned_data = []
        for item in data["data"]:
                # 转换game_mode和scene为可读文本
            readable_game_mode = game_modes.get(item['game_mode'], '未知模式')
            readable_scene = scenes.get(item['scene'], '未知场景')
            readable_hero = heros.get(item['hero_id'], '未知英雄')
            readable_time = time_shift(item['begin_time'])
                
                # 整理数据
            cleaned_item = {
                    '_id': item['_id'],
                    'role_id': item['role_id'],
                    'room_id': item['room_id'],
                    'hero': readable_hero,
                    'game_mode': readable_game_mode,
                    'scene': readable_scene,
                    'begin_time': readable_time,
                    'kill': item['kill'],
                    'damage': item['damage'],
                    'rescue': item['rescue'],
                    'rank': item['rank']
                }
            cleaned_data.append(cleaned_item)
            
        return cleaned_data

        # 执行清洗
    cleaned_data = clean_data(data, game_modes, scenes)

        # 打印清洗后的数据
    for index,item in enumerate(cleaned_data): 
        room_id= item['room_id']
        hero= item['hero']
        game_mode= item['game_mode']
        scene=  item['scene']
        begin_time= item['begin_time']
        kill=item['kill']
        damage=item['damage']
        rescue=item['rescue']
        rank=item['rank']
        print(f"{oldname}的第{index+1}条战绩：房间号{room_id}，英雄{hero}，{game_mode}，{scene}，游戏时间{begin_time}，击杀{kill}，伤害{damage}，救援{rescue}，排名{rank}")

if __name__ == '__main__':
    main()