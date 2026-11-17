"""Native-object layouts for the current two conceptual figures; no raster assets."""
from pathlib import Path
import json, math
R=Path(__file__).resolve().parent
NAVY='#19364D';TEAL='#087F87';GOLD='#B7781D';PURPLE='#795A96';CORAL='#C35F4D';GRAY='#536675'
PALE=['#EAF1F6','#E8F5F3','#FBF2E1','#F1ECF6','#F9EDE8']
class Diagram:
 def __init__(self,zh): self.zh=zh;self.items=[];self.n=0
 def add(self,kind,name,**kw):
  self.n+=1;self.items.append(dict(kind=kind,name=f'{self.n:03d} {name}',**kw))
 def box(self,name,x,y,w,h,fill=None,line=None,rounded=False):self.add('box',name,x=x,y=y,w=w,h=h,fill=fill,line=line,lineWidth=1.3,rounded=rounded)
 def text(self,name,x,y,w,h,t,size=18,color=NAVY,bold=False,align='left'):
  self.add('text',name,x=x,y=y,w=w,h=h,text=t,size=size,color=color,bold=bold,align=align,valign='middle',wrap=True,font='Microsoft YaHei' if self.zh else 'Arial')
 def line(self,name,pts,color=GRAY,arrow=False,dash=False,width=1.8):self.add('wire',name,points=pts,color=color,arrow=arrow,dash=dash,lineWidth=width)
 def ellipse(self,name,x,y,w,h,fill=None,line=NAVY):self.add('ellipse',name,x=x,y=y,w=w,h=h,fill=fill,line=line,lineWidth=1.5)
 def target(self,x,y,c=CORAL):
  self.ellipse('target outer',x-10,y-10,20,20,'#FFFFFF',c);self.ellipse('target centre',x-4,y-4,8,8,c,c)
 def arm(self,x,y,s=1,c=TEAL):
  pts=[[x,y],[x+35*s,y-40*s],[x+90*s,y-18*s]]
  self.line('arm links',pts,'#BFCBD2',width=13*s);self.line('arm contours',pts,NAVY,width=2*s)
  for px,py in pts:self.ellipse('arm joint',px-6*s,py-6*s,12*s,12*s,'#FFFFFF',c)
 def eye(self,x,y,s=1):
  pts=[[x,y+16*s],[x+15*s,y+3*s],[x+30*s,y],[x+45*s,y+3*s],[x+60*s,y+16*s],[x+45*s,y+29*s],[x+30*s,y+32*s],[x+15*s,y+29*s]]
  self.add('polygon','eye outline',points=pts,fill='#FFFFFF',line=NAVY,lineWidth=1.5)
  self.ellipse('iris',x+21*s,y+7*s,18*s,18*s,PALE[1],TEAL);self.ellipse('pupil',x+27*s,y+13*s,6*s,6*s,NAVY,NAVY)
 def cue(self,x,y,c=TEAL):
  self.box('context cue',x,y,36,36,'#FFFFFF',c)
  for a in range(3):
   for b in range(3):
    if (a+b)%2==0:self.box('cue tile',x+3+a*10,y+3+b*10,10,10,c)
 def header(self,title,sub):
  self.text('figure title',24,12,952,38,title,28,bold=True)
  self.text('figure subtitle',24,52,952,28,sub,17,GRAY)
 def save(self,name):
  p=R/(name+'.json');p.write_text(json.dumps(dict(width=1000,height=650,scale=.72,background='#FFFFFF',font='Arial',exportWidth=3000,items=self.items),ensure_ascii=False,indent=2),encoding='utf8')

def fig1(zh):
 d=Diagram(zh);T=lambda en,cn:cn if zh else en
 d.header(T('Evidence for shared and separable learning','共享与分离学习的证据'),T('Locate the shared process across inputs, outputs and timescales','沿输入、输出和时间尺度定位共享发生的环节'))
 titles=[T('Transfer','迁移'),T('Dissociation','分离'),T('Error source','误差来源'),T('Sensory specificity','感觉特异性')]
 captions=[T('Planned compensation\nand rapid correction','预先补偿与快速纠错'),T('Endpoint and online\nfeedback differ','终点反馈与在线反馈'),T('Cursor, hand and\ncontextual cue','光标、手部与情境线索'),T('Vision and\nproprioception','视觉与本体感觉')]
 colors=[NAVY,TEAL,GOLD,PURPLE]
 for i in range(4):
  x=24+i*242;d.box('evidence panel',x,94,226,169,PALE[i]);d.box('evidence accent',x,94,226,4,colors[i]);d.text('evidence heading',x+10,105,206,28,titles[i],21,colors[i],True)
  d.text('evidence observation',x+10,213,206,43,captions[i],17,align='center')
  if i==0:
   d.arm(x+24,192,.75);d.target(x+186,151,TEAL);d.target(x+186,190,CORAL)
   d.line('transfer to planned',[[x+100,173],[x+141,151],[x+171,151]],TEAL,True)
   d.line('transfer to correction',[[x+100,173],[x+141,190],[x+171,190]],CORAL,True)
  if i==1:
   for j in range(2):
    xx=x+18+j*100;d.box('feedback screen',xx,144,85,56,'#FFFFFF',TEAL);d.target(xx+65,156)
    if j:d.line('online trajectory',[[xx+10,190],[xx+29,186],[xx+43,170],[xx+56,164]],TEAL,True)
    else:d.ellipse('endpoint cursor',xx+18,182,7,7,TEAL,TEAL)
  if i==2:
   d.add('polygon','cursor',points=[[x+30,150],[x+30,188],[x+42,177],[x+55,177]],fill=NAVY,line=None)
   d.arm(x+80,192,.65,GOLD);d.cue(x+172,151,GOLD)
  if i==3:d.eye(x+20,158,.9);d.arm(x+120,191,.8,PURPLE)
 d.text('process section',24,274,230,25,T('Learning process','学习过程'),18,bold=True)
 d.box('training context band',229,277,175,28,PALE[1]);d.text('training context',229,277,175,28,T('Training context','训练情境'),16,TEAL,True,'center')
 d.box('test context band',617,277,175,28,PALE[3]);d.text('test context',617,277,175,28,T('Test context','测试情境'),16,PURPLE,True,'center')
 stage=[(T('Error representation','误差表征'),T('Vision / proprioception','视觉／本体感觉')),(T('Update','更新'),T('What changes','什么发生改变')),(T('Memory','记忆'),T('What persists','什么得以保留')),(T('Expression','表达'),T('What is read out','什么被读出')),(T('Movement','运动'),T('Force / kinematics / EMG','力／运动学／肌电'))]
 for i,(h,b) in enumerate(stage):
  x=24+i*194;d.box('learning stage',x,320,176,100,PALE[i],colors[i] if i<4 else CORAL)
  d.text('stage title',x+8,325,160,45,h,18,[NAVY,TEAL,GOLD,PURPLE,CORAL][i],True,'center');d.text('stage meaning',x+7,375,162,40,b,16,align='center')
  if i<4:d.line('process direction',[[x+178,369],[x+192,369]],NAVY,True)
 d.line('training acts on update',[[316,306],[316,318]],TEAL,True);d.line('test acts on expression',[[704,306],[704,318]],PURPLE,True)
 for i,(a,b) in enumerate([(T('Sensory channels','感觉通道'),T('Visual / proprioceptive error','视觉／本体感觉误差')),(T('Control outputs','控制输出'),T('Planned / corrective response','预先补偿／纠错响应')),(T('Timescales','时间尺度'),T('Fast / slow contributions','快／慢成分'))]):
  x=24+i*322;d.box('comparison axis',x,438,308,63,PALE[[1,2,3][i]]);d.text('axis',x+12,442,284,26,a,18,[TEAL,GOLD,PURPLE][i],True);d.text('axis examples',x+12,469,284,25,b,16)
 for i,(a,b) in enumerate([(T('Pair the readouts','配对读出'),T('Correction + next-trial learning','纠错＋下一试次学习')),(T('Cross the contexts','交叉情境'),T('Training cue × test cue','训练线索×测试线索')),(T('Calibrate the inputs','校准输入'),T('Perception + mechanics','感知＋力学'))]):
  x=24+i*322;d.ellipse('measurement number',x,527,32,32,[NAVY,GOLD,PURPLE][i],None);d.text('measurement number',x,527,32,32,str(i+1),18,'#FFFFFF',True,'center');d.text('measurement heading',x+43,523,263,30,a,19,bold=True);d.text('measurement detail',x+43,556,263,36,b,16)
 d.line('footer rule',[[24,609],[976,609]],'#D4DEE5',width=1)
 d.text('scope',24,614,952,24,T('Conceptual ordering of experiments; relationships are hypotheses to test.','实验组织的概念顺序；各环节之间的关系需通过实验检验。'),15,GRAY)
 d.save('figure1_'+('zh' if zh else 'en'))

def fig2(zh):
 d=Diagram(zh);T=lambda en,cn:cn if zh else en
 d.header(T('Measurements that discriminate competing accounts','区分竞争解释的测量'),T('Temporal responses → report calibration → cross-study prediction','时间响应 → 报告校准 → 跨研究预测'))
 # Row 1: common modes, fixed output mixture.
 d.box('temporal panel',24,91,952,167,'#F5F8FA');d.text('temporal title',38,98,900,28,T('a  Resolve temporal mixtures','a  分解时间成分'),21,bold=True)
 d.text('inputs',44,145,165,64,T('Visual input\nProprioceptive input','视觉输入\n本体感觉输入'),17)
 for j,(name,c) in enumerate([(T('Fast mode','快成分'),TEAL),(T('Slow mode','慢成分'),CORAL)]):
  yy=138+j*49;d.box('temporal mode',290,yy,139,36,PALE[1] if j==0 else PALE[4],c,True);d.text('mode label',290,yy,139,36,name,18,c,True,'center')
  d.line('input access',[[213,170],[251,170],[251,yy+18],[286,yy+18]],NAVY,True)
 for j,(name,c) in enumerate([(T('Planned force','预先补偿力'),GOLD),(T('Rapid correction','快速纠错'),PURPLE)]):
  yy=138+j*49;d.box('output',646,yy,283,36,'#FFFFFF',c,True);d.text('output label',653,yy,269,36,name,18,c,True,'center')
 for a in range(2):
  for b in range(2):d.line('fixed readout weight',[[432,156+a*49],[641,156+b*49]],TEAL if a==0 else CORAL,True,width=1.5)
 d.text('fixed readout label',455,126,166,22,T('Fixed readout','固定读出'),15,GRAY,align='center')
 d.text('temporal conclusion',44,227,897,26,T('Changing output ratios can arise from a fixed mixture of fast and slow modes.','快慢成分的固定混合，也能产生随延迟变化的输出比例。'),17,TEAL,True)
 # Row 2: observations are mixtures, human passive movement explicit.
 d.box('calibration panel',24,270,952,173,'#F8F5FA');d.text('calibration title',38,277,900,28,T('b  Calibrate the report contributions','b  校准报告成分'),21,bold=True)
 d.text('human modes',44,319,208,76,T('Robot-guided arm\n(passive movement)\nSelf-generated movement','机器人引导人体手臂\n（被动运动）\n自主运动'),16)
 for j,(name,c) in enumerate([(T('Sensory change','感觉变化'),TEAL),(T('Learned state','学习状态'),CORAL)]):
  yy=313+j*47;d.box('latent contribution',287,yy,158,36,'#FFFFFF',c,True);d.text('latent label',287,yy,158,36,name,17,c,True,'center')
 for j,name in enumerate([T('Passive localization','被动定位报告'),T('Active localization','主动定位报告')]):
  yy=313+j*47;d.box('localization report',659,yy,270,36,'#FFFFFF',PURPLE,True);d.text('report label',665,yy,258,36,name,18,PURPLE,True,'center')
 for a in range(2):
  for b in range(2):d.line('candidate report loading',[[448,331+a*47],[654,331+b*47]],TEAL if a==0 else CORAL,True,True,width=1.5)
 d.text('loading legend',468,302,170,22,T('Candidate loadings','待检验的报告载荷'),15,GRAY,align='center')
 d.text('calibration conclusion',44,408,897,26,T('Independent calibration constrains sensory and learned contributions to each report.','通过独立校准约束每项报告中的感觉与学习状态贡献。'),17,PURPLE,True)
 # Row 3: proper train/freeze/score ordering.
 d.box('prediction panel',24,455,952,145,'#F9F6EE');d.text('prediction title',38,462,900,28,T('c  Predict another study','c  预测另一项研究'),21,bold=True)
 d.box('source data',44,505,166,48,'#FFFFFF',NAVY,True);d.text('source label',44,505,166,48,T('Source study\nFit + select penalty','来源研究\n拟合＋选择惩罚项'),16,NAVY,True,'center')
 d.line('freeze direction',[[214,529],[245,529]],NAVY,True)
 d.box('frozen parameters',249,505,155,48,'#FFFFFF',GOLD,True);d.text('frozen label',249,505,155,48,T('Freeze parameters','冻结参数'),16,GOLD,True,'center')
 d.line('predict direction',[[408,529],[443,529]],NAVY,True)
 d.box('target predictions',447,501,251,60,'#FFFFFF',TEAL,True);d.text('target labels',454,502,237,58,T('Target-study predictions\nCommon / separate modes','目标研究预测\n共同／分别时间成分'),16,TEAL,True,'center')
 d.line('score direction',[[702,529],[737,529]],NAVY,True)
 d.box('heldout score',741,501,188,60,'#FFFFFF',PURPLE,True);d.text('score label',746,502,178,58,T('Score held-out data\nBoth outputs','留出数据评分\n分别评估两个输出'),16,PURPLE,True,'center')
 d.text('prediction conclusion',44,566,897,25,T('Compare complete held-out responses; report model recovery and analysis sensitivity.','比较完整留出响应，同时报告模型恢复和分析敏感性。'),16,GOLD,True)
 d.text('supported inference',24,608,952,30,T('Inference target: transferable input–output dynamics; neural sharing needs selective intervention.','推断目标：可迁移的输入—输出动态；神经共享需选择性干预检验。'),16,NAVY,True)
 d.save('figure2_'+('zh' if zh else 'en'))

for zh in [False,True]:fig1(zh);fig2(zh)
print('Wrote four native-only layouts.')
