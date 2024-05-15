import os

def get_project_root() :
  """
  Projectルートのパスを返却する
  """
  # カレントファイルのフルパス
  current_file_path = os.path.abspath(__file__)

  # カレントファイルがある絶対ディレクトリパス
  current_dir = os.path.dirname(current_file_path)

  # プロジェクトルートのフルパス
  # カレントファイルからさかのぼって、あるディレクトリ数上の絶対パスを取得
  return os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))