# Norminator
from codecs import register_error
import os
import sched
from xml.dom.domreg import registered
import discord
import json
from discord import Client, Intents, Embed
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
#from classList import class_list
import classList

load_dotenv()

# ----------Server Connection---------------------------------------------------------
TOKEN = os.getenv('TOKEN')
guild_ids=[958840606090735636, 959869467926622248]   #<- my AI server
    #test NormNavelBotTest server: 959869467926622248
    # guild_ids=[958840606090735636]   #<- my AI server

# TOKEN (main)= OTU5ODkzMjEzMjA2OTM3NjIw.YkigNw.qOleYXPELILyDkFC3Wa2g5sQzpI
# TOKEN2 (secondary (AI server))= OTU5ODk5NzYzOTEyODY3ODYw.YkimUQ.zXKtDgtKMjHTK7k_2s4ZYXqdyv0

#---------------------------------------------------------------------------------------


intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(960021234052132905)
    await channel.send(
        f'Welcome {member.mention}, please go to the <#960021166213460048> channel to assign yourself roles that correspond to your classes'
    )

@slash.slash(
    name="test",
    description="This is just a test command, nothing more.",
    guild_ids=guild_ids,
    options=[
        create_option(
            name="option1",
            description="choose your word!",
            required=True,
            option_type=3, # option_type 3 = string
            # choices=[
            #     create_choice(
            #         name="World!",
            #         value="world"
            #     ),
            #     create_choice(
            #         name="You!",
            #         value="you"
            #     )
            # ]
        )
    ]
)
async def test(ctx:SlashContext, option1:str):
    await ctx.send(f'Hello {option1}! channel ID test: <#958840606090735639>')
    

@commands.has_permissions(administrator=True)
@slash.slash(name="createrole", description="Create a new role for the server.", guild_ids=guild_ids)
async def test(ctx):
    await ctx.send(content="/createrole str:roleName, str:categoryName, optional: str:channelName")

@commands.has_permissions(administrator=True)
@slash.slash(name="deleterole", description="Delete an existing role from the server.", guild_ids=guild_ids)
async def test(ctx):
    await ctx.send(content="/deleterole str:roleName")



@slash.slash(name="roles", description="View the list of roles.", guild_ids=guild_ids,)
async def roles(ctx):
    await ctx.send(content="/roles optional: str:category")

# -----------------------------------------------------------------------------------------------------
@commands.has_permissions(administrator=True)
@slash.slash(
    name="editrole", 
    description="Change the name of an existing role.", 
    guild_ids=guild_ids,
    options=[
        create_option(
            name="role_to_be_edited",
            description="Choose the Role you want to edit",
            required=True,
            option_type=3, 
        )    
    ]
)
async def edit_role(ctx):
    await ctx.send(content="/editrole str:oldRoleName str:newRoleName")
    # await ctx.send(f'Hello {edit_role}! channel ID test: <#958840606090735639>')




@slash.slash(name="assignrole", description="Assign yourself a role.", guild_ids=guild_ids,
    options=[
        create_option(
            name="role_to_be_assigned",
            description="Choose a role to assign yourself!",
            required=True,
            option_type=3, 
        )
    ]
)
async def assign_role(ctx):
    await ctx.send(content="/assignrole str:role")




@slash.slash(name="unassignrole", description="Unassign yourself a role.", guild_ids=guild_ids,
    options=[
        create_option(
            name="role_to_be_unassigned ",
            description="Choose one of your roles that you want to unnassign",
            required=True,
            option_type=3, 
        )
    ]
)
async def unassign_role(ctx):
    await ctx.send(content="/unassignrole str:role")




@slash.slash(name="linkserver", description="link a server to a class role", guild_ids=guild_ids,
    options=[
        create_option(
            name="url_to_be_linked",
            description="Choose a server to link to your class role",
            required=True,
            option_type=3, 
        )
    ]
)
async def link_server(ctx):
    await ctx.send(content="/linkserver str:role")




@slash.slash(name="unlinkserver", description="unlink all servers from a single class role", guild_ids=guild_ids,
    options=[
        create_option(
            name="role_to_unlink",
            description="Choose a role for which you want to unlink all servers",
            required=True,
            option_type=3, 
        )
    ]
)
async def unlink_server(ctx):
    await ctx.send(content="/unlinkserver str:role")




@commands.has_permissions(administrator=True)
@slash.slash(name="nukeservers", description="unlink all servers from all class role", guild_ids=guild_ids,
    options=[
        create_option(
            name="nuclear_launch_code",
            description="Enter Nuclear Launch code to nuke server",
            required=True,
            option_type=3, 
        )
    ]
)
async def nuke_server(ctx):
    await ctx.send(content="/nukeservers")







# [:+:] -----------------------Addendum -------------------------  [:+:]
                                                

with open("citrusTree.json", 'rb') as file:
    if file.read(2) != '{}':
        file.seek(0)
        classDict = json.load(file)
    else:
        classDict = {}

# schedule= []
# for n in range(61,91+90,9):
#     schedule.append(json.dumps(classDict)[n:n+5])



@slash.slash(
    name="register",
    description="grow your potential",
    guild_ids=guild_ids,
)
# msg = registered course
async def register(ctx:SlashContext):
    await ctx.send(f'Register for a Course: ')

    #await ctx.send(file=file)

    msg = await client.wait_for("message")
    msg_author = msg.author
    msg_author_str = str(msg_author)
    msg = msg.content.lower()
    #msg = msg.capitalize()
    await ctx.send(f'Registered Course:{msg}, Student:{msg_author}')
    
    if msg_author_str in classDict:
        print("Student found, searching for course")
        if(msg_author_str,msg) not in classDict.items():
            print("└─> course NOT found, appending msg input as new course entry")
            classDict[msg_author_str].append(msg)
    else:
        print("Student NOT found, initializing input as new val(?) ")
        classDict[msg_author_str]= [msg]
        

    # registered= classDict[msg_author_str]
    # await ctx.send(f'Registered Courses: {registered}')
    # await ctx.send(f'sched: {schedule}')


    # print("CHECKING SCHEDULE:    ---->")
    # for i in range(len(schedule)-1):
    #     if schedule[i] in registered:
    #         print(" ───> crn found in registered: " + schedule[i])
    #         crn= schedule[i]
    #         crn = "[" + crn + "]"
    #         schedule = schedule[:i]+[crn]+schedule[i+1:]

schedule = []
print("CHECKING SCHEDULE:    ---->")
catalogue = json.dumps(classDict["schedule"])
for i in range(len(catalogue)):
    if catalogue[i] in registered:
        print(" ───> crn found in registered: " + catalogue[i])
        schedule.append("[" + catalogue[i] + "]")
    else:
        schedule.append(catalogue[i])




@slash.slash(
    name="grow",
    description="grow your potential",
    guild_ids=guild_ids,
)
async def grow(ctx:SlashContext):
    await ctx.send(f'Grow your Citrus Tree? (y/n)')
    answer = await client.wait_for("message")
    author = answer.author
    student = str(author)
    ans= answer.content.lower()
    print(" GROW TREE|  ans: " + ans + " student: " + student)
    await ctx.send(f'answer:{ans}, Student:{student}')

      

    schedule = []
    for x in classDict["schedule"]:
        if x in classDict[student]:
            schedule.append("["+ x +"]")
        else:
            schedule.append(x)

    profile = """```ini
    ───────▄▀▀▀▀▀▀▀▀▀▀▄▄
    ────▄▀▀░░░░░░░░░░░░░▀▄
    ──▄▀░░░░░░░░░░░░░░░░░░▀▄
    ──█░░░░░░░░░░░░░░░░░░░░░▀▄
    ─▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌
    ─█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█
    ▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌
    █░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█
    █░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌
    ▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌
    ─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█
    ─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█
    ──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█
    ───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌
    ───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀
    ───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█
    ───▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█
    ───█░░░▀░░░░▀▄░░░░░░░░░░▄▀
    ──▐▌░░░░░░░░░░▀▄░░░░░░▄▀
    ─▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀
    ▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄

    [:+:]──────────────────────────────────────────────────────────────────────────[:+:]
      |   Student: """+str(student)+"""                                                  |
      |   Year: 4                                                                    | 
      |   GPA: 3.58                                                                  | 
      |    Completed Courses: """+str(classDict[student])+"""                            |
    [:+:]──────────────────────────────────────────────────────────────────────────[:+:]
    
             
    ```""" 


    classTree = """```ini
    
    """+schedule[0]+"""
        │               ┌── ------> """+schedule[4]+"""
        │               │
        │       ┌──> """+schedule[3]+"""
        │       │       │
        │       │       └────────── ----------> """+schedule[9]+"""
        │       │ 
        │       │
   [    └───┐───┘──────────────── --------> """+schedule[7]+"""     ]
            │                                ˄                                      
            │          """+schedule[1]+""" ──────────────┘─┐
            │                                  ˅                         
   [    ┌───└──────────────────────── ------> """+schedule[8]+"""                 ]
   [    │                                                                         ]              
   [    │                                                                         ]       
   [ """+schedule[2]+""" ────────────────────── -----> """+schedule[6]+"""        ]                                  
        │                   
        │    
        └────── -----> """+schedule[5]+"""
             
    ```""" 
    await ctx.send(f'{profile} ')
    await ctx.send(f'{classTree} ')
#async def grow(ctx:SlashContext):
    # await ctx.send(f'{classTree}')


        
# [:-:] -----------------------------------------------------------  [:-:]


client.run(TOKEN)