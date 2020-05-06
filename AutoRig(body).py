import maya.cmds as cmds
 
#create joints (body chain) 
cmds.joint(p=(-0.063,102.695,0),n=('root_jnt'))
cmds.joint(p=(-0.188,111.843,0),n=('stomach_jnt'))
cmds.joint(p=(0.188,129.763,0),n=('chest_jnt'))
cmds.joint(p=(-0.063,143.799,0),n=('neck_jnt'))
cmds.joint(p=(0.188,161.969,0),n=('head_jnt'))

#deselect
cmds.select(clear=True)

#create joints (arm chain)
cmds.joint(p=(6.203,138.535,0),n=('L_collarBone_jnt'))
cmds.joint(p=(12.93,137.929,0),n=('L_shoulder_jnt'))
cmds.joint(p=(12.437,-19.609,-1.657),n=('L_elbow_jnt'), r=True) 
cmds.joint(p=(12.408,-14.055,8.077),n=('L_wrist_jnt'),r=True)

#create joints (hand)
cmds.joint(p=(4.238,-4.376,4.094),n=('L_palm_jnt'),r=True)
#thumbJoints
cmds.joint(p=(-5.243,0,2.574),n=('L_Thumb1_jnt'),r=True)
cmds.joint(p=(-0.363,-2.258,2.081),n=('L_Thumb2_jnt'),r=True)
cmds.joint(p=(-0.546,-1.847,1.756),n=('L_Thumb3_jnt'),r=True)
#deselect
cmds.select(clear=True)
#indexJoints
cmds.joint(p=(-0.584,-2.815,3.243),n=('L_Index1_jnt'),r=True)
cmds.joint(p=(0.184,-2.193,1.191),n=('L_Index2_jnt'),r=True)
cmds.joint(p=(0.318,-2.048,0.591),n=('L_Index3_jnt'),r=True)
cmds.joint(p=(0.222,-1.984,1.329),n=('L_Index4_jnt'),r=True)
#parent index1 to palm
cmds.parent('L_Index1_jnt','L_palm_jnt', r=True)
#deselect
cmds.select(clear=True)
#middleJoints
cmds.joint(p=(0.573,-3.412,1.466),n=('L_Middle1_jnt'),r=True)
cmds.joint(p=(0.631,-2.068,1.612),n=('L_Middle2_jnt'),r=True)
cmds.joint(p=(-0.027,-2.546,0.314),n=('L_Middle3_jnt'),r=True)
cmds.joint(p=(0.093,-1.48,0.427),n=('L_Middle4_jnt'),r=True)
#parent Middle1 to palm
cmds.parent('L_Middle1_jnt','L_palm_jnt', r=True)
#deselect
cmds.select(clear=True)
#ringJoints
cmds.joint(p=(1.896,-2.481,0.4531),n=('L_Ring1_jnt'),r=True)
cmds.joint(p=(0.961,-3.413,0.658),n=('L_Ring2_jnt'),r=True)
cmds.joint(p=(0.137,-2.309,0.434),n=('L_Ring3_jnt'),r=True)
cmds.joint(p=(-0.131,-1.728,0.185),n=('L_Ring4_jnt'),r=True)
#parent Ring1 to palm
cmds.parent('L_Ring1_jnt','L_palm_jnt', r=True)

#deselect
cmds.select(clear=True)
#pinkyJoints
cmds.joint(p=(1.807,-2.608,-2.075),n=('L_Pinky1_jnt'),r=True)
cmds.joint(p=(0.299,-2.683,0.581),n=('L_Pinky2_jnt'),r=True)
cmds.joint(p=(0.385,-2.063,0.288),n=('L_Pinky3_jnt'),r=True)
cmds.joint(p=(0.329,-1.935,0.196),n=('L_Pinky4_jnt'),r=True)
#parent Pinky1_jnt to palm
cmds.parent('L_Pinky1_jnt','L_palm_jnt', r=True)

#deselect
cmds.select(clear=True)

#create joints (leg chain)
cmds.joint(p=(8.068,97.25,0),n=('L_hip_jnt'))
cmds.joint(p=(4.206,-39.767,4.584),n=('L_knee_jnt'),r=True)
cmds.joint(p=(3.906,-43.079,-5.7),n=('L_ankle_jnt'),r=True)
cmds.joint(p=(0.403,-10.532,8.135),n=('L_ballOfFoot_jnt'),r=True)
cmds.joint(p=(-0.121,-2.019,4.19),n=('L_toe_jnt'),r=True)

#deselect
cmds.select(clear=True)

#orient joints
cmds.joint('L_hip_jnt',edit=True,orientJoint='xyz',secondaryAxisOrient='zdown',ch=True)
cmds.joint('root_jnt',edit=True,orientJoint='xyz',secondaryAxisOrient='zdown',ch=True)
cmds.joint('L_collarBone_jnt',edit=True,orientJoint='xyz',secondaryAxisOrient='zdown',ch=True)

#mirror leg chain
cmds.mirrorJoint('L_hip_jnt',mirrorYZ=True,mirrorBehavior=True,searchReplace=('L_', 'R_') )

#mirror Arm chain
cmds.mirrorJoint('L_collarBone_jnt',mirrorYZ=True,mirrorBehavior=True,searchReplace=('L_', 'R_') )


