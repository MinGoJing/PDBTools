# PDBTools

PDB�ļ��㼶���������������Դ������㹤�߼���

PDB�ļ���PDBTools�н�������Ϊ4���㼶��Protein -> Chain -> Residue -> Atom

��ע�⣺���ĵ������еġ��Ƕȡ���ָ�����ƽǶȣ����еġ���ת���󡱾�ָ�ҳ���ת����


���������뷽��
==============

��������
--------

* Load(pdbFileName, parseHBool = False)

��PDB�ļ�����ΪProtein����

������
    pdbFileName, str��PDB�ļ���
    parseHBool, bool���Ƿ�����ԭ�ӽ���

����ֵ��
    Protein����


* LoadModel(pdbFileName, parseHBool = False)

������MODEL�ؼ��ʵ�PDB����ΪProtein����list����Щ���׶����name���Խ�������Ϊ��
PDB�ļ��� + '_model_' + MODEL��š�����ͬLoad������

���PDB�в���MODEL�ؼ��ʣ����һ��MODEL�ؼ���֮ǰ�Ծ���ATOM�У����ⲿ��ԭ�ӽ���
����������ֵlist�ĵ�һ��Ԫ���У���name���Խ�������Ϊ��PDB�ļ��� + '_model_0'��

����ֵ��
    Protein����list


* Dumpl(structObjList, dumpFileName, fileMode = 'w')

���κβ㼶���󹹳ɵ�list�����PDB�ļ���

������
    structObjList, list���㼶���󹹳ɵ�list
    dumpFileName, str��PDB�ļ���
    fileMode, str���ļ������ģʽ


* DumpFastal(structObjList, dumpFileName, fileMode = 'w')

����Atom�㼶���󹹳ɵ�list�����Fasta�ļ�������ͬDumpl������


* __init__

���ֽṹ����Ĺ��캯���������£�

Protein(proteinID = '')
Chain(chainName = '', owner = None)
Residue(resName = '', resNum = 0, resIns = '', owner = None)
Atom(atomName = '', atomNum = 0, atomCoord = np.array([0., 0., 0.]), atomIns = '', atomFollowing = '', owner = None)

��������Щ���캯��ʱ�����owner��ΪNone�����캯�����Զ���owner���½ṹ����֮��
����������ϵ��


���в㼶���з���
----------------

* Dump(self, dumpFileName, fileMode = 'w')

��self�����PDB�ļ���

������
    dumpFileName, str������ļ���
    fileMode, str���ļ������ģʽ


* Dumps(self)

�õ��ַ�����ʽ��PDB�ļ����ݡ�


* Copy(self)

�õ�self�������


��Atom�㼶���з���
------------------

* DumpFasta(self, dumpFileName, fileMode = 'w')

��self�����fasta�ļ�������ͬDump������


* GetResidues(self), IGetResidues(self)

��㼶ֱ�ӷ���self���������вл��������У�GetResidues��������list��IGetResidues
����������������


* GetAtoms(self), IGetAtoms(self)

��㼶ֱ�ӷ���self����������ԭ�Ӷ������У�GetAtoms��������list��IGetAtoms����
������������


* FilterAtoms(self, atomName = 'CA', *atomNameTuple), IFilterAtoms(self, atomName = 'CA', *atomNameTuple)

��㼶ֱ�Ӱ�һ������ԭ����ɸѡself����������ԭ�Ӷ������У�FilterAtoms������
��list��IFilterAtoms����������������

structObj.FilterAtoms()  # ɸѡCAԭ�ӣ�Ĭ�ϣ�
structObj.FilterAtoms('N', 'CA', 'C')  # ɸѡ�Ǽ�ԭ��


* GetAtomsCoord(self)

��㼶ֱ�ӷ���self����������ԭ�ӵ����꣨N*3 ndarray����


* FilterAtomsCoord(self, atomName = 'CA', *atomNameTuple)

��㼶ֱ�Ӱ�һ������ԭ����ɸѡself����������ԭ�Ӷ��󣬷���ɸѡ�������ԭ�ӵ�
���꣨N*3 ndarray����


* RenumResidues(self, startNum = 1), RenumAtoms(self, startNum = 1)

��self���������вл�/ԭ�ӽ����ر�š�startNum���������趨��ʼ��š�


* MoveCenter(self)

����ƽ��self��ʹ��self�ļ�������ƽ����ԭ�㡣


* Append(self, *appendObjTuple), Insert(self, idxNum, *insertObjTuple)

Ϊself׷��/�����ӽṹ�����������self���ӽṹ����ԭ�ṹ�������Copy�����õ��Ŀ�����
�һ���self�Զ�����������ϵ��

������
    *appendObjTuple, *insertObjTuple, *obj��self��Ӧ���ӽṹ���󣨲�����������
    idxNum, int������λ������ֵ


��Protein�㼶���з���
---------------------

* Remove(self)

�ӽṹ������ɾ��self����


�������
========

����
----

��Atom�����ֱ�ӵ������Ӷ����ʵ�ǰ�㼶���Ӳ㼶�����б�

for chainObj in structObj:
    for resObj in chainObj:
        for atomObj in resObj:
            pass


��Ƭ
----

��Atom�������Ƭ��

structObj[:]        # ��ȡ������
structObj[0][1:]    # ��ȡ�л�����
structObj[0][0][0]  # ��ȡԭ�Ӷ���


����
----

��Atom����ɵ���len�����������ӽṹ�б�ĳ��ȣ�

len(structObj)


����ֵ
------

��Atom����Ĳ���ֵ�������Ƿ�Ϊ�սṹ�����ж����������self.subΪ[]���򲼶�ֵΪ
False������ΪTrue��

Atom����Ĳ���ֵһ��ΪTrue��


ŷ�Ͼ���
--------

ԭ�Ӷ��������˼������������������ԭ��֮���ŷ�Ͼ��룺

atomObjA - atomObjB


����
====

���в㼶��������
----------------

* name, str

�����Զ��ڲ�ͬ�Ĳ㼶���岻ͬ��
Protein��PDB�ļ�����������".pdb"��չ����
Chain������
Residue���л���
Atom��ԭ����


��Atom�㼶��������
------------------

* sub, list

self���Ӳ㼶�����б�


* center, ndarray (ֻ��)
self������ԭ�����꼸�����ġ�


* seq, str (ֻ��)

self�Ĳл�����


* fasta, str (ֻ��)

self��fasta�ļ��ַ���


��Protein�㼶��������
---------------------

* owner, obj

self�ĸ�������


* idx, int (ֻ��)

self����owner��sub�е�����ֵ


* pre, next, obj (ֻ��)

self��ǰ/��һ��ͬ�㼶����
���selfû��ǰ/��һ���������׳�IndexError


������������
------------

* subDict, dict (ֻ��)

Protein��Residue�㼶���У�����ֱ�Ϊ��
Protein����self��������������ɵ�����-�������ϣ��
Residue����self������ԭ�Ӷ�����ɵ�ԭ����-ԭ�Ӷ����ϣ��


* num, int

Residue��Atom�㼶���У�����ֱ�Ϊ��
Residue�������������ַ��Ĳл����
Atom��ԭ�����


Residue��������
---------------

* ins, str

�л������ַ�


* compNum, str (���ⷽʽд)

�л���� + �л������ַ�

������ͨ��(num, ins)��Ԫ����и�ֵ��

resObj.compNum = (1, '')


* coordDict, dict (ֻ��)

��self������ԭ����ɵ�ԭ����-ԭ�������ϣ��


Atom��������
------------

* coord, ndarray

ԭ������


* alt, str

����λ��ָʾ��


* occ, str

ռ��


* tempF, str

�¶�����


* ele, str

Ԫ�ط���


* chg, str

���


�л������
==========

�л�����ʵ�������ɶԵ�����������ǽ��м��㡢��ת��صķ��������������з�����self
��רָResidue���󣩡�

���������
----------

���������в���ʱ��ע�⣺���N����C�˵������л��ֱ��޷����ж����PHI��PSI�ļ���
���������Ϊ����������ǲ����ڣ����������������������׳�IndexError��

* CalcBBDihedralAngle(self, dihedralSideStr)

������������ǡ�

������
    dihedralSideStr, str��������������ࡣl/phi��ʾPHI�������ַ�����ʾPSI������
�ִ�Сд��


* CalcBBRotationMatrixByDeltaAngle(self, dihedralSideStr, modifySideStr, deltaAngle)

����ת�Ƕ���Ϊ����������������ת����

������
    dihedralSideStr��ͬCalcBBDihedralAngle������
    modifySideStr, str��ת���ࡣl/n��ʾ��N�˽�����ת�������ַ�����ʾ��C�˽�����
ת�������ִ�Сд��
    deltaAngle, float��ת���Ƕȡ�

����ֵ��
    moveCoord, ndarray(1*3)����תǰ/��ƽ������
    rotationMatrix, ndarray(3*3)����ת����


* CalcBBRotationMatrixByTargetAngle(self, dihedralSideStr, modifySideStr, targetAngle)

��Ŀ��Ƕ���Ϊ����������������ת����

�����뷵��ֵͬCalcBBRotationMatrixByDeltaAngle��������targetAngle��ʾĿ��Ƕȡ�


* GetBBRotationAtomObj(self, dihedralSideStr, modifySideStr)

��ȡ�Ը�������������תʱ��������Ҫ��ת��ԭ�Ӷ��󡣲���ͬCalcBBRotationMatrixByDeltaAngle
������

����ֵ��
    rotationAtomObjList, list��ԭ�Ӷ���list


* RotateBBDihedralAngleByDeltaAngle(self, dihedralSideStr, modifySideStr, deltaAngle)

����ת�Ƕ���Ϊ����ֱ����ת����������ͬCalcBBRotationMatrixByDeltaAngle������


* RotateBBDihedralAngleByTargetAngle(self, dihedralSideStr, modifySideStr, targetAngle)

��Ŀ��Ƕ���Ϊ����ֱ����ת����������ͬCalcBBRotationMatrixByTargetAngle������


���������
----------

�Բ������е���ʱ��ע�⣺GLY��ALA�л����ڲ����ڲ�������ǣ����ɵ������з������Ҳ�
��ʹ�ò����ڵĲ������������ֵ�������з������������������������׳�IndexError��

* CalcSCDihedralAngle(self, dihedralIdx)

�����������ǡ�

������
    dihedralIdx, int���������������ֵ������ֵ��0��ʼ��ţ������������ֵ���ݲ�
���������ͬ������ֵ��ʾĳ���л������������������ϵĵ�N����������ǡ�


* CalcSCRotationMatrixByDeltaAngle(self, dihedralIdx, deltaAngle)

����ת�Ƕ���Ϊ���������������ת����

������
    dihedralIdx��ͬCalcSCDihedralAngle����
    deltaAngle����ת�Ƕ�

����ֵͬCalcBBRotationMatrixByDeltaAngle������


* CalcSCRotationMatrixByTargetAngle(self, dihedralIdx, targetAngle)

��Ŀ��Ƕ���Ϊ���������������ת���󡣲����뷵��ֵͬCalcSCRotationMatrixByDeltaAngle
��������targetAngle��ʾĿ��Ƕȡ�


* GetSCRotationAtomObj(self, dihedralIdx)

��ȡ�Ը�����������ǽ�����תʱ��������Ҫ��ת��ԭ�Ӷ��󡣲���ͬCalcSCDihedralAngle
����������ֵͬGetBBRotationAtomObj������


* RotateSCDihedralAngleByDeltaAngle(self, dihedralIdx, deltaAngle)

����ת�Ƕ���Ϊ����ֱ����ת����������ͬCalcSCRotationMatrixByDeltaAngle������


* RotateSCDihedralAngleByTargetAngle(self, dihedralIdx, targetAngle)

��Ŀ��Ƕ���Ϊ����ֱ����ת����������ͬCalcSCRotationMatrixByTargetAngle������


��ѧ����
========

* Dis(coordA, coordB)

����������ά����֮���ŷʽ���롣


* Norm(coordArray)

����һ����ά����Ķ�������


* CalcVectorAngle(coordA, coordB)

�����������нǣ����ؽǶȣ�0 ~ pi����


* CalcRotationMatrix(rotationAxis, rotationAngle)

���������ת����

������
    rotationAxis, ndarray(1*3)����ת��������������������λ����
    rotationAngle, float����ת��


* CalcRotationMatrixByTwoVector(coordA, coordB)

���������A��ת������B����Ҫ����ת����


* CalcDihedralAngle(coordA, coordB, coordC, coordD)

�������ǡ������з��ŽǶȣ�-pi ~ pi����


* CalcRMSD(coordArrayA, coordArrayB)

����RMSD��

������
    coordArrayA, coordArrayB, ndarray(N*3)����������ά������ɵĵȳ���ά����


* CalcSuperimposeRotationMatrix(sourceCoordArray, targetCoordArray)

�����sourceCoordArray��targetCoordArray�ĵ�����ת����

������
    sourceCoordArray, targetCoordArray, ndarray(N*3)����������ά������ɵĵȳ�
��ά����

����ֵΪƽ������sourceCenterCoord����ת����rotationMatrix���Լ�ƽ������targetCenterCoord��
ʹ��sourceCoordArrayͨ��(sourceCoordArray - sourceCenterCoord).dot(rotationMatrix) + targetCenterCoord
������ƽ��->��ת->ƽ�Ʋ�������targetCoordArray�γɵ��ϡ�


����
====

* RESIDUE_NAME_THREE_TO_ONE_DICT, RESIDUE_NAME_ONE_TO_THREE_DICT

����ĸ������ĸ�л������໥ת����ϣ��


����˵��
========

��������
--------

����������Load��LoadModel������ȫ����PDB�ļ���ATOM�еĳ���˳���PDB�ļ����н���
��洢����������κ�������̡�

Load�����ڽ���ʱ�������κη�ATOM��ͷ���С���LoadModel�����������κη�ATOM��MODEL
��ͷ���С�


���ڴ����²㼶������ж�
------------------------

* Load������
    Protein��ֻ���ڽ�����ʼǰ����Ψһ��һ���������շ����������
    Chain���ڽ�����ʼʱ���Լ�ÿ�μ�⵽���������仯ʱ������һ��ATOM�е���ǰ�У�����
�ᴴ���µ�������
    Residue���ڽ�����ʼʱ���Լ�ÿ�μ�⵽�л������л���Ż�л������ַ�����֮һ����
�仯ʱ������һ��ATOM�е���ǰ�У������ᴴ���µĲл�����
    Atom��ÿ��⵽һ���µ�ATOM�ж��ᴴ��һ��Atom����

* LoadModel������
    Protein��������ʼǰ���Լ�ÿ�μ�⵽MODEL�ؼ���ʱ���ᴴ��һ���µĵ��׶���
���������ʼǰ�����ĵ��׶���Ϊ�գ���������ķ���ֵ�б�ɾ����
    Chain��������ʼʱ��ÿ�μ�⵽���������仯ʱ������һ��ATOM�е���ǰ�У����Լ�
һ���µ�Model����ʱ�����ᴴ���µ�������
    Residue��������ʼʱ��ÿ�μ�⵽�л������л���Ż�л������ַ�����֮һ������
��ʱ������һ��ATOM�е���ǰ�У����Լ�һ���µ�Model����ʱ�����ᴴ���µĲл�����
    Atom��ÿ��⵽һ���µ�ATOM�ж��ᴴ��һ��Atom����


���ֶ�
------

����ʱ��������ַ������Խ���strip�������������еĿ��ֶζ��ᱻ����Ϊ���ַ�����
��������ɸѡ�������޸�ʱ�������á�


__slots__
---------

�������ܵĿ��ǣ��ĸ��ṹ�඼������__slots__���ʲ�������������޶���������ԡ�


δ������Ϊ
----------

���ĵ���δ�ἰ�ģ��Լ����Բ����ϲ㼶�ṹ�Ĳ���������л�׷�������󣬵���ԭ�Ӷ���
�ȣ�����Ϊ����δ����ġ����ܻ��������������δ֪���⡣�������ܵĿ��ǣ�������δ��
����ʱ�ĸ��ֲ�������Ϊ��ȫ������ͼ������Ϊ��顣