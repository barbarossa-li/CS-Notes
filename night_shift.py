"""便利店夜班：一场会分叉的文字冒险。

运行：python3 night_shift.py
输入选项前的数字继续，输入 q 可以下班。
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Scene:
    text: str
    choices: tuple[tuple[str, str], ...] = ()
    ending: bool = False


BANNER = """
==============================
  便利店夜班：第三位客人
==============================
凌晨的自动门不该响第三次。
输入选项前的数字。输入 q 可以下班。
""".strip()


SCENES: dict[str, Scene] = {
    "start": Scene(
        text=(
            "凌晨 3:07，便利店的自动门响了。\n"
            "监控里今晚只进来过两个人，但这是第三声铃。\n"
            "门口站着一个穿旧制服的人，胸口的店名和你这家店一样，款式却像是十年前的。"
        ),
        choices=(
            ("说「欢迎光临」", "welcome"),
            ("用手电筒照他", "flashlight"),
            ("给店长打电话", "call"),
        ),
    ),
    "welcome": Scene(
        text=(
            "他把帽子抬起来。脸和你有点像，只是更疲倦。\n"
            "「我来交班。你的班已经上完了。」\n"
            "墙上的钟跳了一下，停在 3:07。"
        ),
        choices=(
            ("把工牌递给他", "mirror"),
            ("告诉他你不认识他", "receipt"),
            ("问上一班的收银差额", "change"),
        ),
    ),
    "mirror": Scene(
        text=(
            "工牌放到他手心时变热了。\n"
            "柜台后的镜子里，你的表情正在慢慢变成他的。\n"
            "他看着镜子，像在等你点头。"
        ),
        choices=(
            ("接受这张新面孔", "ending_handover"),
            ("砸碎镜子", "ending_smash"),
            ("问镜子你到底是谁", "ending_question"),
        ),
    ),
    "flashlight": Scene(
        text=(
            "光穿过他的身体，落在货架上。\n"
            "那里多出一排没有条码的罐头，标签上印着你今晚做过的事：\n"
            "擦柜台、加热便当、对着冰柜发呆。"
        ),
        choices=(
            ("打开一罐", "ending_can"),
            ("把罐头放回去，并道歉", "ending_polite"),
            ("把整排罐头扫进购物车结账", "checkout"),
        ),
    ),
    "checkout": Scene(
        text=(
            "收款机开始打印。小票很长，而且没有停下来的意思。\n"
            "每扫一罐，货架就再长出一罐。\n"
            "数字跳得比你的心跳还快。"
        ),
        choices=(
            ("继续扫，直到它承认你赢了", "ending_forever"),
            ("拔掉收款机的电源", "ending_unplug"),
            ("边打小票边吃一罐", "ending_meal"),
        ),
    ),
    "call": Scene(
        text=(
            "店长秒接。听筒里是同一首店内音乐。\n"
            "他说：「你不是在跟我打电话。你在跟上一班的自己打电话。」\n"
            "门口那个人也看着你，像听得见。"
        ),
        choices=(
            ("问他怎么离开这班", "leave"),
            ("挂断，把这句话告诉门口的人", "ending_promote"),
            ("让店长立刻过来", "ending_loop"),
        ),
    ),
    "leave": Scene(
        text=(
            "店长的声音低下去：「对着空无一人的门口，说一次欢迎光临。说完别回头。」\n"
            "旧制服的人已经不在原地，只剩下门铃还在轻轻晃。"
        ),
        choices=(
            ("照做，说完不回头", "ending_fourth"),
            ("回头看门口，再把话说完", "ending_echo"),
            ("改对冷柜说欢迎光临", "ending_freezer"),
        ),
    ),
    "ending_handover": Scene(
        text=(
            "你点了点头。镜子里的脸彻底换成了他的，而他本人消失了。\n"
            "你站到门口，工牌温热，像刚从别人手里接过来。\n"
            "远处有脚步声。下一班的人快到了。\n\n"
            "【结局：交班】有人总会来接夜班。"
        ),
        ending=True,
    ),
    "ending_smash": Scene(
        text=(
            "镜子碎了一地。警报短促地叫了一声，又自己安静下去。\n"
            "旧制服的人被碎光吓退，退进自动门，第三声铃倒着响了一遍。\n"
            "钟从 3:07 走到 3:08。你的脸还是你的。\n\n"
            "【结局：碎镜】有些交接，拒绝了就不算数。"
        ),
        ending=True,
    ),
    "ending_question": Scene(
        text=(
            "你问镜子。镜子先开口，用你的声音问了同一句。\n"
            "两个人都答不上来。旧制服的人耸耸肩，把工牌放回柜台。\n"
            "「那今晚就先别交班了。」他走进员工通道，通道尽头是一面新的镜子。\n\n"
            "【结局：问题本身】你保住了自己，也保住了这个没答案的夜班。"
        ),
        ending=True,
    ),
    "receipt": Scene(
        text=(
            "他并不生气，只是掏出一张小票。\n"
            "时间印的是明天，商品名称是你的名字，备注写着「已离职」。\n"
            "你还没找到笔，小票底部已经出现了你的签名。\n\n"
            "【结局：明天的小票】你被一个还没发生的自己辞退了。"
        ),
        ending=True,
    ),
    "change": Scene(
        text=(
            "差额是 0 元。明细最后一行却写着「时间 × 1」。\n"
            "他笑了一下，把那一行从机器里抽出来，折成纸鹤放进你的口袋。\n"
            "钟重新走动。门外开始下雨，他走进雨里，门铃没有再响。\n\n"
            "【结局：找零成功】这一夜终于被允许结束。"
        ),
        ending=True,
    ),
    "ending_can": Scene(
        text=(
            "罐头里没有食物，只有一个早晨：阳光、面包机、你哼着走调的歌。\n"
            "你眨眼，发现自己站在白天的店里，工装是干的。\n"
            "夜班像一段没保存的录音，只在舌尖留下一点金属味。\n\n"
            "【结局：被叫醒】有些夜班只发生在罐头里。"
        ),
        ending=True,
    ),
    "ending_polite": Scene(
        text=(
            "你把罐头放回原位，说了句对不起。\n"
            "他点点头，侧身走进冷柜，门自己合上。监控上的人数跳回 2。\n"
            "冷柜玻璃上留下一个手印，一会儿就化了。\n\n"
            "【结局：礼貌的鬼】道歉有时候比光更有用。"
        ),
        ending=True,
    ),
    "ending_forever": Scene(
        text=(
            "你扫到第 40 罐时，小票已经拖到地上。\n"
            "收款机心满意足地响了一声，然后又吐出一行：继续。\n"
            "你忽然明白，这个夜班的编制写的是「收银员（无限期）」。\n\n"
            "【结局：永不打烊】贪心的人会获得稳定的工作。"
        ),
        ending=True,
    ),
    "ending_unplug": Scene(
        text=(
            "电源拔掉的一瞬间，整店暗了。小票停在半空。\n"
            "黑暗里那个人轻轻说了句辛苦了，然后散成货架上的灰尘。\n"
            "窗外先白了一线。你把电源插回去，灯亮了，罐头恢复成泡面。\n\n"
            "【结局：拔电源】有的账，不记才算结清。"
        ),
        ending=True,
    ),
    "ending_meal": Scene(
        text=(
            "你打开一罐。里面是热的便当，味道和你两小时前加热的那份一样。\n"
            "小票还在打印，但你已经坐下吃了。旧制服的人在对面也坐下来，分走一双筷子。\n"
            "你们谁也没说话。吃完后他擦了擦嘴，把空罐放进回收箱，夜班就算交接完毕。\n\n"
            "【结局：加班餐】最好的交班仪式，是一起把饭吃完。"
        ),
        ending=True,
    ),
    "ending_promote": Scene(
        text=(
            "你挂断电话，把店长的话重复给门口的人。\n"
            "他认真听完，把帽子戴到你头上。\n"
            "「那就由你来当店长。下一班如果又响了第三声铃，记得接电话。」\n"
            "你的手机变成对讲机，里面循环播放店内音乐。\n\n"
            "【结局：晋升】管理夜班的人，通常也是夜班本身。"
        ),
        ending=True,
    ),
    "ending_loop": Scene(
        text=(
            "玻璃门再次打开。进来的人穿着同样的旧制服，脸却是你的。\n"
            "你们同时说出「欢迎光临」，又同时愣住。\n"
            "钟仍停在 3:07。电话还没挂，听筒里你听见自己正在第三次拨号。\n\n"
            "【结局：两个人的夜班】你和上一班成功会师了，可惜谁也走不了。"
        ),
        ending=True,
    ),
    "ending_fourth": Scene(
        text=(
            "你对着空门口说：「欢迎光临。」说完没有回头。\n"
            "铃响了第四次。进来的是风，还有很淡的天亮。\n"
            "旧制服的人在你身后举起手，算是打过卡，然后消失在货架之间。\n\n"
            "【结局：第四声铃】出口是一句客气话。"
        ),
        ending=True,
    ),
    "ending_echo": Scene(
        text=(
            "你回头。门口站着的是你自己，嘴巴和你同步，把「欢迎光临」说完了。\n"
            "两句话叠在一起，门铃响成一声长音。\n"
            "等声音停下来，门口只剩你的倒影贴在玻璃上，天已经亮了半边。\n\n"
            "【结局：回声】你把自己迎进了第二天。"
        ),
        ending=True,
    ),
    "ending_freezer": Scene(
        text=(
            "你对着冷柜说：「欢迎光临。」\n"
            "冷柜里雾气散开，一个穿旧制服的人坐在存货中间，认真回你：「欢迎光临。」\n"
            "他拍拍旁边的纸箱，示意你下班后可以来坐。门外的铃再也没响。\n\n"
            "【结局：冷柜夜班】你找到了店里最安静的同事。"
        ),
        ending=True,
    ),
}


def choose(scene: Scene) -> str | None:
    """读取一次选择。返回下一场景编号；玩家输入 q 时返回 None。"""
    while True:
        raw = input("你的选择：").strip().lower()
        if raw == "q":
            return None
        if raw.isdigit():
            index = int(raw)
            if 1 <= index <= len(scene.choices):
                return scene.choices[index - 1][1]
        print("请输入选项前的数字。")


def play() -> None:
    scene_id = "start"
    while True:
        scene = SCENES[scene_id]
        print()
        print(scene.text)
        if scene.ending:
            print()
            return
        print()
        for index, (label, _) in enumerate(scene.choices, 1):
            print(f"  {index}. {label}")
        print()
        nxt = choose(scene)
        if nxt is None:
            print()
            print("你把钥匙放回抽屉。夜班还在继续。")
            print()
            return
        scene_id = nxt


def main() -> None:
    print(BANNER)
    while True:
        play()
        again = input("再值一班？(y/n) ").strip().lower()
        if again != "y":
            print("天亮了。")
            return


if __name__ == "__main__":
    main()
