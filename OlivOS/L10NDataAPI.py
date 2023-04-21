# -*- encoding: utf-8 -*-
'''
_______________________    ________________
__  __ \__  /____  _/_ |  / /_  __ \_  ___/
_  / / /_  /  __  / __ | / /_  / / /____ \
/ /_/ /_  /____/ /  __ |/ / / /_/ /____/ /
\____/ /_____/___/  _____/  \____/ /____/

@File      :   OlivOS/L10NDataAPI.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2023, OlivOS-Team
@Desc      :   None
'''

import OlivOS

formatOffsetLimit = 10
flagL10NSelection = 'zh-CN'
flagL10NSelectionDefault = 'en-US'

dictL10NSTR = {
    'en-US': {
        'diagnoseAPI_0001': 'Welcome to OlivOS {0}',
        'diagnoseAPI_0002': 'OlivOS diagnose logger [{0}] is running',
        'accountAPI_0001': 'init account from default ... done',
        'accountAPI_0002': 'init account from [{0}] ... done',
        'accountAPI_0003': 'init account from [{0}] ... failed',
        'accountAPI_0004': 'generate [{0}] account [{1}] as [{2}] ... done',
        'accountAPI_0005': 'generate account ... all done',
        'pluginAPI_0001': 'OlivOS plugin shallow [{0}] is running',
        'pluginAPI_0002': 'OlivOS plugin shallow [{0}] will restart',
        'pluginAPI_0003': 'OlivOS plugin shallow [{0}] call restart',
        'pluginAPI_0004': 'OlivOS plugin shallow [{0}] call check update',
        'pluginAPI_0005': 'Account [{0}] not found, please check your account config',
        'pluginAPI_0006': 'event [{0}] call plugin [{1}] done',
        'pluginAPI_0007': 'event [{0}] call blocked by plugin [{1}]',
        'pluginAPI_0008': 'OlivOS plugin [{0}] call [{1}] failed: {2}\n{3}',
        'pluginAPI_0009': 'OlivOS plugin [{0}] call [{1}] done',
        'pluginAPI_0010': 'OlivOS plugin [{0}] is skiped by OlivOS plugin shallow [{1}]: {2}\n{3}',
        'pluginAPI_0011': 'OlivOS plugin [{0}] is support for old OlivOS version {1}',
        'pluginAPI_0012': 'is support for old OlivOS version {0}',
        'pluginAPI_0013': 'OlivOS plugin [{0}] is skiped by OlivOS plugin shallow [{1}]: {2}',
        'pluginAPI_0014': 'OlivOS plugin [{0}] is loaded by OlivOS plugin shallow [{1}]',
        'pluginAPI_0015': 'Total count [{0}] OlivOS plugin is loaded by OlivOS plugin shallow [{1}]',
        'onebotV12LinkServerAPI_0001': 'OlivOS onebotV12 link server [{0}] is running',
        'onebotV12LinkServerAPI_0002': 'OlivOS onebotV12 link server [{0}] websocket link will retry in {1}s',
        'onebotV12LinkServerAPI_0003': 'OlivOS onebotV12 link server [{0}] websocket link error',
        'onebotV12LinkServerAPI_0004': 'OlivOS onebotV12 link server [{0}] websocket link close',
        'onebotV12LinkServerAPI_0005': 'OlivOS onebotV12 link server [{0}] websocket link start',
        'onebotV12LinkServerAPI_0006': 'OlivOS onebotV12 link server [{0}] websocket link lost',
        'hackChatLinkServerAPI_0001': 'OlivOS hackChat link server [{0}] is running',
        'hackChatLinkServerAPI_0002': 'OlivOS hackChat link server [{0}] websocket link will retry in {1}s',
        'hackChatLinkServerAPI_0003': 'OlivOS hackChat link server [{0}] websocket link error',
        'hackChatLinkServerAPI_0004': 'OlivOS hackChat link server [{0}] websocket link close',
        'hackChatLinkServerAPI_0005': 'OlivOS hackChat link server [{0}] websocket link start',
        'hackChatLinkServerAPI_0006': 'OlivOS hackChat link server [{0}] websocket link lost',
        'updateAPI_0001': 'will check {0} lib after {1}s ...',
        'updateAPI_0002': 'check {0} lib patch target md5: [{1}]',
        'updateAPI_0003': 'check {0} lib patch [{1}] md5: [{2}]',
        'updateAPI_0004': 'download new {0} lib ...',
        'updateAPI_0005': 'download new {0} lib FAILED! md5 check FAILED!',
        'updateAPI_0006': 'check {0} lib patch api FAILED! try later please!',
        'updateAPI_0007': 'download {0} lib patch FAILED! try later please!',
        'updateAPI_0008': 'update {0} lib patch [{1}] -> [{2}]',
        'updateAPI_0009': 'update {0} lib patch done!',
        'updateAPI_0010': '{0} lib already latest!',
        'updateAPI_0011': '{0} lib update FORCESKIP!',
        'updateAPI_0012': 'download new {0} lib done',
        'updateAPI_0013': 'check OlivOS update ......',
        'updateAPI_0014': 'OlivOS already latest.',
        'updateAPI_0015': 'check OlivOS update api error, skip update replace.',
        'updateAPI_0016': 'check OlivOS update file hit, will run update replace.',
        'updateAPI_0017': 'check OlivOS update file not hit, skip update replace.',
        'updateAPI_0018': 'OlivOS running in src mode, skip update replace.',
        'updateAPI_0019': 'OlivOS update found.',
        'updateAPI_0020': 'OlivOS update found, please try update.',
        'libWQEXEModelAPI_0001': 'OlivOS libWQEXEModel server [{0}] can`t found target lib',
        'libWQEXEModelAPI_0002': 'OlivOS libWQEXEModel server [{0}] will run under visiable mode',
        'libWQEXEModelAPI_0003': 'OlivOS libWQEXEModel server [{0}] will retry in 10s...',
        'libWQEXEModelAPI_0004': 'OlivOS libWQEXEModel failed: {0}\n{1}',
        'libEXEModelAPI_0001': 'OlivOS libEXEModel server [{0}] can`t found target lib',
        'libEXEModelAPI_0002': 'OlivOS libEXEModel server [{0}] will run under visiable mode',
        'libEXEModelAPI_0003': 'OlivOS libEXEModel server [{0}] will retry in 10s...',
        'libEXEModelAPI_0004': 'OlivOS libEXEModel failed: {0}\n{1}',
        'libEXEModelAPI_0005': 'OlivOS libEXEModel server [{0}] is running',
        'libEXEModelAPI_0006': 'OlivOS libEXEModel server [{0}] exited',
        'flaskServerAPI_0001': 'OlivOS flask server [{0}] is running',
        'libCWCBEXEModelAPI_0001': 'OlivOS libCWCBEXEModel server [{0}] can`t found target lib',
        'libCWCBEXEModelAPI_0002': 'OlivOS libCWCBEXEModel server [{0}] will run under visiable mode',
        'libCWCBEXEModelAPI_0003': 'OlivOS libCWCBEXEModel server [{0}] will retry in 10s...',
        'libCWCBEXEModelAPI_0004': 'OlivOS libCWCBEXEModel failed: {0}\n{1}',
        'libCWCBEXEModelAPI_0005': 'OlivOS libCWCBEXEModel server [{0}] is running',
        'libCWCBEXEModelAPI_0006': 'OlivOS libCWCBEXEModel server [{0}] exited',
        'bootAPI_0001': 'OlivOS model [{0}] will init',
        'bootAPI_0002': 'OlivOS model [{0}] init',
        'bootAPI_0003': 'OlivOS model [{0}] will try init',
        'bootAPI_0004': 'OlivOS model [{0}] type init',
        'bootAPI_0005': 'OlivOS model [{0}] stopped',
        'bootAPI_0006': 'OlivOS model [{0}] will stop',
    },
    'zh-CN': {
        'diagnoseAPI_0001': '欢迎使用 青果核心交互栈 OlivOS {0}',
        'diagnoseAPI_0002': 'OlivOS 日志组件 [{0}] 正在运作',
        'accountAPI_0001': '从默认配置装载账号 ... 完成',
        'accountAPI_0002': '从配置存档 [{0}] 装载账号 ... 完成',
        'accountAPI_0003': '从配置存档 [{0}] 装载账号 ... 失败',
        'accountAPI_0004': '进行 [{0}] 账号装载，从 [{1}] 至 [{2}] ... 完成',
        'accountAPI_0005': '进行账号装载 ... 全部完成',
        'pluginAPI_0001': 'OlivOS 插件组件 [{0}] 正在运作',
        'pluginAPI_0002': 'OlivOS 插件组件 [{0}] 即将重载',
        'pluginAPI_0003': 'OlivOS 插件组件 [{0}] 发起重载',
        'pluginAPI_0004': 'OlivOS 插件组件 [{0}] 发起更新检查',
        'pluginAPI_0005': '账号 [{0}] 未找到, 请检查你的账号配置',
        'pluginAPI_0006': '事件 [{0}] 调用插件 [{1}] 完成',
        'pluginAPI_0007': '事件 [{0}] 被插件 [{1}] 拦截，将终止后续插件处理',
        'pluginAPI_0008': 'OlivOS 插件 [{0}] 调用 [{1}] 失败: {2}\n{3}',
        'pluginAPI_0009': 'OlivOS 插件 [{0}] 调用 [{1}] 完成',
        'pluginAPI_0010': 'OlivOS 插件 [{0}] 被 OlivOS 插件组件 [{1}] 跳过: {2}\n{3}',
        'pluginAPI_0011': 'OlivOS 插件 [{0}] 专为旧版 OlivOS 版本 {1} 设计',
        'pluginAPI_0012': '专为旧版 OlivOS 版本 {0} 设计',
        'pluginAPI_0013': 'OlivOS 插件 [{0}] 被 OlivOS 插件组件 [{1}] 跳过: {2}',
        'pluginAPI_0014': 'OlivOS 插件 [{0}] 被 OlivOS 插件组件 [{1}] 加载',
        'pluginAPI_0015': '共 [{0}] 个 OlivOS 插件被 OlivOS 插件组件 [{1}] 加载',
        'onebotV12LinkServerAPI_0001': 'OlivOS onebotV12 连接服务组件 [{0}] 正在运作',
        'onebotV12LinkServerAPI_0002': 'OlivOS onebotV12 连接服务组件 [{0}] WebSocket 连接 将在{1}秒内重试',
        'onebotV12LinkServerAPI_0003': 'OlivOS onebotV12 连接服务组件 [{0}] WebSocket 连接 发生错误',
        'onebotV12LinkServerAPI_0004': 'OlivOS onebotV12 连接服务组件 [{0}] WebSocket 连接 已经关闭',
        'onebotV12LinkServerAPI_0005': 'OlivOS onebotV12 连接服务组件 [{0}] WebSocket 连接 已经启动',
        'onebotV12LinkServerAPI_0006': 'OlivOS onebotV12 连接服务组件 [{0}] WebSocket 连接 已经丢失',
        'hackChatLinkServerAPI_0001': 'OlivOS hackChat 连接服务组件 [{0}] 正在运作',
        'hackChatLinkServerAPI_0002': 'OlivOS hackChat 连接服务组件 [{0}] WebSocket 连接 将在{1}秒内重试',
        'hackChatLinkServerAPI_0003': 'OlivOS hackChat 连接服务组件 [{0}] WebSocket 连接 发生错误',
        'hackChatLinkServerAPI_0004': 'OlivOS hackChat 连接服务组件 [{0}] WebSocket 连接 已经关闭',
        'hackChatLinkServerAPI_0005': 'OlivOS hackChat 连接服务组件 [{0}] WebSocket 连接 已经启动',
        'hackChatLinkServerAPI_0006': 'OlivOS hackChat 连接服务组件 [{0}] WebSocket 连接 已经丢失',
        'updateAPI_0001': '将在 {1}秒后 检查 {0} 依赖库 ...',
        'updateAPI_0002': '检查 {0} 依赖库补丁 目标 MD5文件摘要: [{1}]',
        'updateAPI_0003': '检查 {0} 依赖库补丁 [{1}] MD5文件摘要: [{2}]',
        'updateAPI_0004': '下载新的 {0} 依赖库 ...',
        'updateAPI_0005': '下载新的 {0} 依赖库 失败! MD5文件摘要检查失败!',
        'updateAPI_0006': '访问 {0} 依赖库补丁网络接口 失败! 请稍后再试!',
        'updateAPI_0007': '下载 {0} 依赖库补丁 失败! 请稍后再试!',
        'updateAPI_0008': '更新 {0} 依赖库补丁 [{1}] -> [{2}]',
        'updateAPI_0009': '更新 {0} 依赖库补丁 完成!',
        'updateAPI_0010': '{0} 依赖库 已是最新!',
        'updateAPI_0011': '{0} 依赖库更新 强制跳过(FORCESKIP)!',
        'updateAPI_0012': '下载新的 {0} 依赖库 完成',
        'updateAPI_0013': '检查 OlivOS 更新 ......',
        'updateAPI_0014': 'OlivOS 已是最新。',
        'updateAPI_0015': '检查 OlivOS 更新接口失败, 跳过更新',
        'updateAPI_0016': '检查 OlivOS 更新文件命中, 即将更新',
        'updateAPI_0017': '检查 OlivOS 更新文件未命中, 跳过更新',
        'updateAPI_0018': '检测到 OlivOS 在源码模式下运行, 跳过更新',
        'updateAPI_0019': '发现 OlivOS 版本更新',
        'updateAPI_0020': '发现 OlivOS 版本更新，请尝试进行一键更新',
        'libWQEXEModelAPI_0001': 'OlivOS WQ进程托管服务组件 [{0}] 无法找到库文件',
        'libWQEXEModelAPI_0002': 'OlivOS WQ进程托管服务组件 [{0}] 将在前台模式下运行',
        'libWQEXEModelAPI_0003': 'OlivOS WQ进程托管服务组件 [{0}] 将在10秒后重试...',
        'libWQEXEModelAPI_0004': 'OlivOS WQ进程托管服务组件 错误: {0}\n{1}',
        'libEXEModelAPI_0001': 'OlivOS GoCq进程托管服务组件 [{0}] 无法找到库文件',
        'libEXEModelAPI_0002': 'OlivOS GoCq进程托管服务组件 [{0}] 将在前台模式下运行',
        'libEXEModelAPI_0003': 'OlivOS GoCq进程托管服务组件 [{0}] 将在10秒后重试...',
        'libEXEModelAPI_0004': 'OlivOS GoCq进程托管服务组件 错误: {0}\n{1}',
        'libEXEModelAPI_0005': 'OlivOS GoCq进程托管服务组件 [{0}] 正在运作',
        'libEXEModelAPI_0006': 'OlivOS GoCq进程托管服务组件 [{0}] 已经存在',
        'flaskServerAPI_0001': 'OlivOS onebotV11 flask POST服务组件 [{0}] 正在运作',
        'libCWCBEXEModelAPI_0001': 'OlivOS ComWeChatBotClient进程托管服务组件 [{0}] 无法找到库文件',
        'libCWCBEXEModelAPI_0002': 'OlivOS ComWeChatBotClient进程托管服务组件 [{0}] 将在前台模式下运行',
        'libCWCBEXEModelAPI_0003': 'OlivOS ComWeChatBotClient进程托管服务组件 [{0}] 将在10秒后重试...',
        'libCWCBEXEModelAPI_0004': 'OlivOS ComWeChatBotClient进程托管服务组件 错误: {0}\n{1}',
        'libCWCBEXEModelAPI_0005': 'OlivOS ComWeChatBotClient进程托管服务组件 [{0}] 正在运作',
        'libCWCBEXEModelAPI_0006': 'OlivOS ComWeChatBotClient进程托管服务组件 [{0}] 已经存在',
        'bootAPI_0001': 'OlivOS 组件 [{0}] 即将初始化',
        'bootAPI_0002': 'OlivOS 组件 [{0}] 初始化',
        'bootAPI_0003': 'OlivOS 组件 [{0}] 即将尝试初始化',
        'bootAPI_0004': 'OlivOS 组件 [{0}] 类型 即将初始化',
        'bootAPI_0005': 'OlivOS 组件 [{0}] 已被停止',
        'bootAPI_0006': 'OlivOS 组件 [{0}] 即将停止',
    }
}
